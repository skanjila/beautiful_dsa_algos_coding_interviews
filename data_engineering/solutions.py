from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Iterable, List, Sequence


Row = Dict[str, Any]


def _parse_timestamp(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    if isinstance(value, str):
        normalized = value.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(normalized)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    raise TypeError(f"Unsupported timestamp value: {value!r}")


def deduplicate_latest(
    rows: Sequence[Row],
    key_field: str = "event_id",
    order_field: str = "ingested_at",
) -> List[Row]:
    """Keep the latest row per business key using a deterministic tie-break."""
    latest_by_key: Dict[Any, Row] = {}

    for row in rows:
        key = row[key_field]
        current_best = latest_by_key.get(key)
        if current_best is None or _parse_timestamp(row[order_field]) >= _parse_timestamp(
            current_best[order_field]
        ):
            # Copy so callers do not mutate the original input through the result.
            latest_by_key[key] = dict(row)

    return sorted(latest_by_key.values(), key=lambda row: (row[key_field], row[order_field]))


def top_n_per_group(
    rows: Sequence[Row],
    group_field: str,
    value_field: str,
    n: int,
) -> List[Row]:
    """Return the top N rows per group ordered by descending value."""
    grouped: Dict[Any, List[Row]] = defaultdict(list)
    for row in rows:
        grouped[row[group_field]].append(dict(row))

    result: List[Row] = []
    for _, group_rows in sorted(grouped.items(), key=lambda item: item[0]):
        ordered = sorted(group_rows, key=lambda row: row[value_field], reverse=True)
        result.extend(ordered[:n])
    return result


def daily_active_users(
    rows: Sequence[Row],
    timestamp_field: str = "event_ts",
    user_field: str = "user_id",
) -> List[Row]:
    """Count unique active users per UTC business day."""
    users_by_day: Dict[str, set[Any]] = defaultdict(set)

    for row in rows:
        day = _parse_timestamp(row[timestamp_field]).date().isoformat()
        users_by_day[day].add(row[user_field])

    return [
        {"event_date": day, "daily_active_users": len(users)}
        for day, users in sorted(users_by_day.items())
    ]


def sessionize_events(
    rows: Sequence[Row],
    user_field: str = "user_id",
    timestamp_field: str = "event_ts",
    threshold_minutes: int = 30,
) -> List[Row]:
    """Assign session numbers using an inactivity gap threshold."""
    threshold = timedelta(minutes=threshold_minutes)
    grouped: Dict[Any, List[Row]] = defaultdict(list)

    for row in rows:
        grouped[row[user_field]].append(dict(row))

    output: List[Row] = []
    for _, user_rows in sorted(grouped.items(), key=lambda item: item[0]):
        ordered = sorted(user_rows, key=lambda row: _parse_timestamp(row[timestamp_field]))
        previous_ts: datetime | None = None
        session_number = 0

        for row in ordered:
            event_ts = _parse_timestamp(row[timestamp_field])
            if previous_ts is None or event_ts - previous_ts > threshold:
                session_number += 1
            previous_ts = event_ts

            row["session_number"] = session_number
            output.append(row)

    return output


def scd_type_2_upsert(
    current_rows: Sequence[Row],
    incoming_rows: Sequence[Row],
    business_key: str,
    tracked_fields: Iterable[str],
    effective_ts: str,
) -> List[Row]:
    """Expire changed current rows and append fresh versions."""
    tracked_fields = list(tracked_fields)
    effective_value = effective_ts

    output = [dict(row) for row in current_rows]
    current_by_key = {
        row[business_key]: row
        for row in output
        if row.get("is_current", True)
    }

    for incoming in incoming_rows:
        key = incoming[business_key]
        existing = current_by_key.get(key)

        if existing is None:
            new_row = dict(incoming)
            new_row["start_ts"] = effective_value
            new_row["end_ts"] = None
            new_row["is_current"] = True
            output.append(new_row)
            current_by_key[key] = new_row
            continue

        has_changed = any(existing.get(field) != incoming.get(field) for field in tracked_fields)
        if not has_changed:
            continue

        existing["end_ts"] = effective_value
        existing["is_current"] = False

        new_row = dict(incoming)
        new_row["start_ts"] = effective_value
        new_row["end_ts"] = None
        new_row["is_current"] = True
        output.append(new_row)
        current_by_key[key] = new_row

    return sorted(output, key=lambda row: (row[business_key], row.get("start_ts") or ""))


def incremental_hourly_sales(
    rows: Sequence[Row],
    watermark_ts: str,
    timestamp_field: str = "event_ts",
) -> List[Row]:
    """Aggregate only rows at or after the watermark into hourly buckets."""
    watermark = _parse_timestamp(watermark_ts)
    aggregates: Dict[tuple[str, Any], Dict[str, Any]] = {}

    for row in rows:
        event_ts = _parse_timestamp(row[timestamp_field])
        if event_ts < watermark:
            continue

        hour_bucket = event_ts.replace(minute=0, second=0, microsecond=0).isoformat()
        store_id = row["store_id"]
        aggregate_key = (hour_bucket, store_id)

        if aggregate_key not in aggregates:
            aggregates[aggregate_key] = {
                "hour_bucket": hour_bucket,
                "store_id": store_id,
                "total_sales": 0,
                "order_ids": set(),
            }

        aggregates[aggregate_key]["total_sales"] += row["amount"]
        aggregates[aggregate_key]["order_ids"].add(row["order_id"])

    results: List[Row] = []
    for key in sorted(aggregates):
        aggregate = aggregates[key]
        results.append(
            {
                "hour_bucket": aggregate["hour_bucket"],
                "store_id": aggregate["store_id"],
                "total_sales": aggregate["total_sales"],
                "order_count": len(aggregate["order_ids"]),
            }
        )
    return results


def identify_late_arriving_events(
    rows: Sequence[Row],
    processed_through_ts: str,
    event_time_field: str = "event_ts",
    ingestion_time_field: str = "ingested_at",
) -> List[Row]:
    """Return rows whose business event time predates the processed watermark."""
    processed_through = _parse_timestamp(processed_through_ts)
    late_rows: List[Row] = []

    for row in rows:
        event_ts = _parse_timestamp(row[event_time_field])
        ingested_at = _parse_timestamp(row[ingestion_time_field])

        if event_ts < processed_through <= ingested_at:
            # The event belongs to an already-closed business window but arrived later.
            late_rows.append(dict(row))

    return sorted(late_rows, key=lambda row: _parse_timestamp(row[ingestion_time_field]))
