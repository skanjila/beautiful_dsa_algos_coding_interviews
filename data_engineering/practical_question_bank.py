from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class PracticalQuestion:
    slug: str
    category: str
    difficulty: str
    question: str
    interview_approach: str
    pandas_approach: str
    spark_approach: str
    deep_dive: str


PRACTICAL_QUESTION_BANK: List[PracticalQuestion] = [
    PracticalQuestion(
        slug="deduplicate-events",
        category="data-cleaning",
        difficulty="easy",
        question="Given an events table with duplicate rows or duplicate event IDs, how would you deduplicate it while keeping the latest record?",
        interview_approach="Start by clarifying the deduplication key and tie-break rule. Say out loud whether duplicates are exact-row duplicates or business-key duplicates like `event_id`. Then define the ordering column, usually ingestion timestamp or event timestamp, before discussing implementation.",
        pandas_approach="Use `sort_values` by the tie-break timestamp, then call `drop_duplicates(subset=['event_id'], keep='last')`. If exact duplicates matter first, run `drop_duplicates()` before business-key dedup. For large in-memory frames, call out that Pandas is fine for prototyping or local analysis but not for production-scale distributed data.",
        spark_approach="Use a window partitioned by `event_id` and ordered by the tie-break timestamp descending. Add `row_number()`, filter to `row_number = 1`, and drop the helper column. Mention that this scales across partitions and is the standard distributed pattern for deterministic deduplication.",
        deep_dive="The real interview signal is not the syntax; it is whether you define deterministic business rules. If timestamps can tie, mention a secondary tie-break such as ingestion sequence or source priority. Also mention whether dedup should happen before or after schema normalization and whether late-arriving events may force reprocessing.",
    ),
    PracticalQuestion(
        slug="top-n-per-group",
        category="aggregation",
        difficulty="medium",
        question="How would you find the top 3 highest-value transactions per customer?",
        interview_approach="Translate the problem into partitioning plus ranking. Say that the key is 'per customer' and the ordering is by transaction value descending. Then state whether ties should be kept, broken, or arbitrarily limited.",
        pandas_approach="Use `sort_values(['customer_id', 'amount'], ascending=[True, False])`, then `groupby('customer_id').head(3)`. For explicit rank semantics, compute `rank` or `cumcount` after sorting. Mention memory constraints if the dataset is too large for one machine.",
        spark_approach="Use a window partitioned by `customer_id` ordered by `amount` descending. Compute `row_number`, `rank`, or `dense_rank` depending on tie semantics, then filter to the top 3. This is the standard distributed answer because it preserves per-group ranking cleanly.",
        deep_dive="Interviewers often care about tie handling more than the top-N syntax. Explain the difference between `row_number`, `rank`, and `dense_rank`, and connect the choice to business expectations. If the downstream consumer needs exactly three rows per user, `row_number` is usually the right answer.",
    ),
    PracticalQuestion(
        slug="daily-active-users",
        category="aggregation",
        difficulty="easy",
        question="How would you compute daily active users from an events table?",
        interview_approach="Clarify the grain first: one user counted once per day. Then identify the event timestamp column and the timezone rule used to derive the business day. Under pressure, say that the solution is 'truncate to day, deduplicate users within the day, then count'.",
        pandas_approach="Convert timestamps to datetime, derive a `event_date` column with `.dt.floor('D')` or timezone-aware normalization, then use `drop_duplicates(['event_date', 'user_id'])` followed by `groupby('event_date').size()`. Mention timezone correctness explicitly because DAU definitions often use business-local time.",
        spark_approach="Use `to_date` or `date_trunc` on the event timestamp, select distinct `(event_date, user_id)` pairs, and aggregate with `count(*)` per day. This is a simple but strong distributed pattern because distinct plus group-by mirrors the business definition directly.",
        deep_dive="The tricky part is semantic correctness. DAU depends on timezone, bot filtering, valid event types, and identity stitching. Mention those assumptions explicitly. A strong answer also notes that this metric may later be extended into rolling 7-day or 28-day active users.",
    ),
    PracticalQuestion(
        slug="sessionization",
        category="window-functions",
        difficulty="hard",
        question="How would you turn clickstream events into user sessions using a 30-minute inactivity threshold?",
        interview_approach="State that this is a window-function problem. Partition by user, order by event time, compare each event to the previous event, and start a new session when the gap exceeds 30 minutes. Saying that structure early shows control.",
        pandas_approach="Sort by `user_id` and event time, compute the previous event time with `groupby('user_id')['event_ts'].shift(1)`, calculate the minute gap, mark a session start when the gap is null or greater than 30, then `cumsum` that start flag per user to create a session ID.",
        spark_approach="Use a user-partitioned ordered window with `lag(event_ts)`. Compute the time difference, flag new sessions when the gap is null or above threshold, then use a cumulative sum over the ordered window to assign session numbers. Mention that Spark SQL window functions are the idiomatic solution here.",
        deep_dive="Sessionization tests whether you can think in ordered state transitions, not just aggregations. Strong answers mention out-of-order events, timezone normalization, and whether the 30-minute rule is event time or ingestion time. If streaming comes up, explain that watermarking and state timeout policy matter.",
    ),
    PracticalQuestion(
        slug="scd-type-2-upsert",
        category="modeling",
        difficulty="hard",
        question="How would you implement a Slowly Changing Dimension Type 2 load for customer attributes?",
        interview_approach="Begin with the business meaning: preserve history rather than overwrite. Then define the natural key, tracked attributes, effective start date, effective end date, and current-row flag. Under pressure, framing the semantics first prevents random SQL or DataFrame code.",
        pandas_approach="Join incoming rows to the current active dimension rows on the business key. Identify changed records by comparing tracked attributes. For changed records, expire the old row by setting its end date and current flag to false, then append a new current row with a fresh effective start date. Mention that Pandas is mainly useful for demonstration or smaller-scale batch processing.",
        spark_approach="Use a merge/upsert pattern if the table format supports it, such as Delta Lake or Iceberg merge semantics. Detect changed rows, update current records to expire them, and insert new versioned rows. If merge is not available, split the flow into unchanged, expired, and new records and rewrite the affected partitions carefully.",
        deep_dive="SCD Type 2 is as much about modeling discipline as code. You should mention idempotency, late arriving dimensions, surrogate keys, and how to avoid opening duplicate current rows for the same business key. In an interview, a crisp explanation of row states often matters more than exact syntax.",
    ),
    PracticalQuestion(
        slug="incremental-aggregation",
        category="pipeline-design",
        difficulty="medium",
        question="How would you design an incremental pipeline to compute hourly sales aggregates without recomputing all history every run?",
        interview_approach="Call out the partition grain immediately: hourly buckets. Then explain that the pipeline should process only new or changed source data for affected buckets and merge results into a target aggregate table. The key interview move is to speak in terms of input windows and output keys.",
        pandas_approach="For a bounded local workflow, filter input rows to the relevant watermark window, derive an hourly bucket, aggregate with `groupby`, and merge the resulting aggregates into the target table keyed by bucket and entity dimensions. Explicitly say that Pandas is illustrative here rather than the default production tool for large-scale recurring jobs.",
        spark_approach="Read only source partitions after the last processed watermark or affected by CDC changes, compute hourly aggregates, then merge or overwrite only the impacted output partitions. Mention partition pruning, watermark management, and idempotent reruns for the same hour.",
        deep_dive="The interview signal is whether you think incrementally instead of defaulting to full refresh. Strong answers mention watermark persistence, late-arriving corrections, idempotent writes, and how to backfill a subset of hours when logic changes.",
    ),
    PracticalQuestion(
        slug="late-arriving-data",
        category="pipeline-reliability",
        difficulty="medium",
        question="How would you handle late-arriving events in a batch or streaming data pipeline?",
        interview_approach="Start by defining what 'late' means relative to business event time and SLA. Then explain whether the system reopens historical partitions, keeps a correction window, or routes late data to a reconciliation path. Interviewers want to hear the policy, not just the code.",
        pandas_approach="In a batch-oriented local flow, identify records whose event date falls into already-processed windows, then rerun or patch only the impacted partitions. Pandas is mostly a good way to prototype the logic for recomputation windows and correction handling.",
        spark_approach="In batch, reprocess impacted partitions or merge corrected aggregates. In streaming, use watermarks, allowed lateness, and state retention to balance completeness with operational cost. Mention that very late data may go through a separate backfill path rather than the hot pipeline.",
        deep_dive="Late data handling is about product policy and platform capability. Strong answers mention event time versus ingestion time, watermark thresholds, cost of reopening old partitions, and the consequences for downstream consumers if historical metrics are revised.",
    ),
    PracticalQuestion(
        slug="skewed-join",
        category="performance",
        difficulty="hard",
        question="How would you diagnose and mitigate a heavily skewed join in Spark?",
        interview_approach="Say that skew shows up when a small number of keys dominate work on a few partitions. Start with diagnosis: task duration imbalance, large shuffle partitions, or stage stragglers. Then propose targeted mitigations rather than generic tuning.",
        pandas_approach="In Pandas, skew is less about distributed execution and more about memory blowups on high-frequency keys. You can profile key distributions with `value_counts`, isolate hot keys, and reason about whether the join should be pre-aggregated or split. Make it clear that Pandas is mainly for diagnosis or smaller datasets here.",
        spark_approach="Profile key frequency, then consider salting hot keys, pre-aggregating before the join, broadcasting the smaller side if appropriate, or using adaptive query execution and skew-join optimizations. Strong answers mention that not every skew problem is solved by increasing cluster size.",
        deep_dive="The most important signal is that you understand skew as a data-distribution problem. Good answers tie mitigation to the physical plan and key distribution. If only one or two keys dominate, salting or special-casing them may outperform broad cluster-wide tuning.",
    ),
]


def list_categories() -> List[str]:
    return sorted({entry.category for entry in PRACTICAL_QUESTION_BANK})


def filter_by_category(category: str) -> List[PracticalQuestion]:
    normalized = category.strip().lower()
    return [entry for entry in PRACTICAL_QUESTION_BANK if entry.category == normalized]


def filter_by_difficulty(difficulty: str) -> List[PracticalQuestion]:
    normalized = difficulty.strip().lower()
    return [entry for entry in PRACTICAL_QUESTION_BANK if entry.difficulty == normalized]


def search_questions(term: str) -> List[PracticalQuestion]:
    normalized = term.strip().lower()
    if not normalized:
        return PRACTICAL_QUESTION_BANK[:]
    return [
        entry
        for entry in PRACTICAL_QUESTION_BANK
        if normalized in entry.question.lower()
        or normalized in entry.interview_approach.lower()
        or normalized in entry.pandas_approach.lower()
        or normalized in entry.spark_approach.lower()
        or normalized in entry.deep_dive.lower()
        or normalized in entry.slug.lower()
        or normalized in entry.category.lower()
    ]


def get_question_by_slug(slug: str) -> Optional[PracticalQuestion]:
    normalized = slug.strip().lower()
    for entry in PRACTICAL_QUESTION_BANK:
        if entry.slug == normalized:
            return entry
    return None


def render_markdown_study_guide() -> str:
    sections = ["# Data Engineering Practical Interview Problems", ""]
    for category in list_categories():
        sections.append(f"## {category.replace('-', ' ').title()}")
        sections.append("")
        for entry in filter_by_category(category):
            sections.append(f"### {entry.question}")
            sections.append(f"- Difficulty: `{entry.difficulty}`")
            sections.append(f"- Interview approach: {entry.interview_approach}")
            sections.append(f"- Pandas approach: {entry.pandas_approach}")
            sections.append(f"- Spark approach: {entry.spark_approach}")
            sections.append(f"- Deep dive: {entry.deep_dive}")
            sections.append("")
    return "\n".join(sections)
