import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from data_engineering.solutions import (
    daily_active_users,
    deduplicate_latest,
    identify_late_arriving_events,
    incremental_hourly_sales,
    scd_type_2_upsert,
    sessionize_events,
    top_n_per_group,
)


def test_deduplicate_latest_keeps_latest_version():
    rows = [
        {"event_id": "a", "ingested_at": "2025-01-01T00:00:00Z", "payload": 1},
        {"event_id": "a", "ingested_at": "2025-01-01T01:00:00Z", "payload": 2},
        {"event_id": "b", "ingested_at": "2025-01-01T00:30:00Z", "payload": 3},
    ]

    result = deduplicate_latest(rows)

    assert result == [
        {"event_id": "a", "ingested_at": "2025-01-01T01:00:00Z", "payload": 2},
        {"event_id": "b", "ingested_at": "2025-01-01T00:30:00Z", "payload": 3},
    ]


def test_top_n_per_group_orders_within_each_group():
    rows = [
        {"customer_id": "c1", "amount": 20},
        {"customer_id": "c1", "amount": 50},
        {"customer_id": "c1", "amount": 10},
        {"customer_id": "c2", "amount": 5},
        {"customer_id": "c2", "amount": 15},
    ]

    result = top_n_per_group(rows, group_field="customer_id", value_field="amount", n=2)

    assert result == [
        {"customer_id": "c1", "amount": 50},
        {"customer_id": "c1", "amount": 20},
        {"customer_id": "c2", "amount": 15},
        {"customer_id": "c2", "amount": 5},
    ]


def test_daily_active_users_counts_unique_users_per_day():
    rows = [
        {"user_id": 1, "event_ts": "2025-01-01T01:00:00Z"},
        {"user_id": 1, "event_ts": "2025-01-01T03:00:00Z"},
        {"user_id": 2, "event_ts": "2025-01-01T04:00:00Z"},
        {"user_id": 1, "event_ts": "2025-01-02T01:00:00Z"},
    ]

    assert daily_active_users(rows) == [
        {"event_date": "2025-01-01", "daily_active_users": 2},
        {"event_date": "2025-01-02", "daily_active_users": 1},
    ]


def test_sessionize_events_starts_new_session_after_gap():
    rows = [
        {"user_id": "u1", "event_ts": "2025-01-01T00:00:00Z"},
        {"user_id": "u1", "event_ts": "2025-01-01T00:20:00Z"},
        {"user_id": "u1", "event_ts": "2025-01-01T01:10:00Z"},
    ]

    result = sessionize_events(rows, threshold_minutes=30)

    assert [row["session_number"] for row in result] == [1, 1, 2]


def test_scd_type_2_upsert_expires_changed_row_and_inserts_new_version():
    current = [
        {
            "customer_id": "c1",
            "segment": "small",
            "status": "active",
            "start_ts": "2025-01-01T00:00:00Z",
            "end_ts": None,
            "is_current": True,
        }
    ]
    incoming = [{"customer_id": "c1", "segment": "enterprise", "status": "active"}]

    result = scd_type_2_upsert(
        current,
        incoming,
        business_key="customer_id",
        tracked_fields=["segment", "status"],
        effective_ts="2025-02-01T00:00:00Z",
    )

    assert len(result) == 2
    assert result[0]["is_current"] is False
    assert result[0]["end_ts"] == "2025-02-01T00:00:00Z"
    assert result[1]["is_current"] is True
    assert result[1]["segment"] == "enterprise"


def test_incremental_hourly_sales_filters_before_watermark_and_aggregates():
    rows = [
        {
            "event_ts": "2025-01-01T00:15:00Z",
            "store_id": "s1",
            "amount": 10,
            "order_id": "o1",
        },
        {
            "event_ts": "2025-01-01T00:45:00Z",
            "store_id": "s1",
            "amount": 15,
            "order_id": "o2",
        },
        {
            "event_ts": "2025-01-01T01:15:00Z",
            "store_id": "s1",
            "amount": 7,
            "order_id": "o3",
        },
    ]

    result = incremental_hourly_sales(rows, watermark_ts="2025-01-01T00:30:00Z")

    assert result == [
        {
            "hour_bucket": "2025-01-01T00:00:00+00:00",
            "store_id": "s1",
            "total_sales": 15,
            "order_count": 1,
        },
        {
            "hour_bucket": "2025-01-01T01:00:00+00:00",
            "store_id": "s1",
            "total_sales": 7,
            "order_count": 1,
        },
    ]


def test_identify_late_arriving_events_finds_retroactive_business_events():
    rows = [
        {
            "event_ts": "2025-01-01T10:00:00Z",
            "ingested_at": "2025-01-02T01:00:00Z",
            "event_id": "late",
        },
        {
            "event_ts": "2025-01-02T03:00:00Z",
            "ingested_at": "2025-01-02T03:01:00Z",
            "event_id": "on-time",
        },
    ]

    result = identify_late_arriving_events(rows, processed_through_ts="2025-01-02T00:00:00Z")

    assert [row["event_id"] for row in result] == ["late"]
