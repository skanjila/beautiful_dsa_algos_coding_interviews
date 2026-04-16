from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class QuestionAnswer:
    slug: str
    category: str
    difficulty: str
    question: str
    short_answer: str
    deep_dive: str


QUESTION_BANK: List[QuestionAnswer] = [
    QuestionAnswer(
        slug="etl-vs-elt",
        category="fundamentals",
        difficulty="easy",
        question="What is the difference between ETL and ELT?",
        short_answer="ETL transforms data before loading it into the destination. ELT loads raw data first and transforms it inside the target warehouse or lakehouse.",
        deep_dive="ETL fits older warehouse patterns where compute was scarce or tightly controlled in the target system. ELT is common in modern cloud analytics stacks because warehouses can scale compute independently and support SQL-based transformation after landing raw data. In interviews, the right answer ties the choice to scale, governance, latency, and reprocessability rather than treating one as universally better.",
    ),
    QuestionAnswer(
        slug="batch-vs-streaming",
        category="fundamentals",
        difficulty="easy",
        question="What is the difference between batch processing and stream processing?",
        short_answer="Batch processing works on bounded datasets at intervals, while stream processing handles unbounded event flows continuously or in near real time.",
        deep_dive="Batch systems are easier to reason about and often simpler operationally, making them a good default for many analytics workloads. Streaming is valuable when freshness matters, such as fraud detection, monitoring, or event-driven product features. Strong interview answers discuss lateness, ordering, state management, replay, and the cost of always-on pipelines.",
    ),
    QuestionAnswer(
        slug="data-lake-vs-warehouse",
        category="storage",
        difficulty="easy",
        question="What is the difference between a data lake and a data warehouse?",
        short_answer="A data lake stores raw or semi-structured data cheaply and flexibly, while a data warehouse emphasizes structured, curated, query-optimized analytics data.",
        deep_dive="A data lake is usually cheaper and better for broad ingestion, archival, and machine-learning-oriented workflows. A warehouse emphasizes cleaned, modeled data and predictable SQL performance. Modern lakehouse systems blur the line by adding table formats, transaction logs, and query optimizations to lake storage. In interviews, explain what part of the lifecycle each store serves and who the primary consumers are.",
    ),
    QuestionAnswer(
        slug="partitioning",
        category="storage",
        difficulty="medium",
        question="Why does partitioning matter in data engineering?",
        short_answer="Partitioning reduces how much data needs to be scanned and moved, improving cost and query performance when it matches common filter patterns.",
        deep_dive="Partitioning works best when aligned with common predicates such as event date, tenant, or region. Bad partitioning can create tiny files, skew, or full-table scans. Good answers mention both physical partitioning and logical bucketing, and they stress that partition keys should be chosen from real access patterns, not generic advice.",
    ),
    QuestionAnswer(
        slug="small-files-problem",
        category="storage",
        difficulty="medium",
        question="Why is the small-files problem harmful in distributed data platforms?",
        short_answer="Too many tiny files increase metadata overhead, task scheduling cost, and inefficient I/O, which slows reads and writes.",
        deep_dive="Distributed systems like Spark or object-store-backed query engines pay a fixed cost per file for listing, planning, and opening readers. Thousands of small files can dominate job runtime even when the total data volume is modest. Practical mitigations include compaction, optimized write sizing, and ingestion patterns that avoid tiny micro-batches landing as independent files.",
    ),
    QuestionAnswer(
        slug="schema-evolution",
        category="modeling",
        difficulty="medium",
        question="What is schema evolution and why does it matter?",
        short_answer="Schema evolution is the controlled ability to add, deprecate, or change fields over time without breaking downstream systems.",
        deep_dive="In real pipelines, producers change before every consumer can adapt. Schema evolution matters because brittle contracts turn small source changes into major outages. Strong answers mention backward compatibility, explicit versioning, nullable additions, default values, and tooling such as schema registries or table-format metadata that enforce rules.",
    ),
    QuestionAnswer(
        slug="slowly-changing-dimensions",
        category="modeling",
        difficulty="medium",
        question="What are slowly changing dimensions and when would you use Type 2?",
        short_answer="Slowly changing dimensions track changes to descriptive attributes over time. Type 2 preserves history by inserting new rows with effective date ranges.",
        deep_dive="Type 2 is valuable when historical correctness matters, such as 'what was the customer segment when the order was placed?'. It increases storage and join complexity but preserves analytical truth over time. Good answers distinguish between overwriting current-state dimensions and preserving historical snapshots, and they connect the choice to reporting requirements.",
    ),
    QuestionAnswer(
        slug="star-schema",
        category="modeling",
        difficulty="easy",
        question="What is a star schema and why is it common in analytics systems?",
        short_answer="A star schema organizes metrics in fact tables surrounded by descriptive dimension tables, which simplifies reporting and BI queries.",
        deep_dive="Star schemas are effective because they align with common analytical thinking: facts answer 'what happened' and dimensions answer 'by whom, where, when, or what category'. They trade some normalization for usability and performance. Strong answers note that star schemas are especially helpful when many analysts and dashboards need a shared semantic model.",
    ),
    QuestionAnswer(
        slug="cdc",
        category="ingestion",
        difficulty="medium",
        question="What is change data capture and why is it useful?",
        short_answer="CDC captures inserts, updates, and deletes from source systems incrementally so downstream systems do not need full reloads every time.",
        deep_dive="CDC reduces source pressure, cuts latency, and improves freshness for downstream warehouses or event pipelines. But it introduces ordering, deletion semantics, snapshot bootstrap, and idempotency concerns. Good answers mention log-based CDC, initial backfills, and how consumers reconcile out-of-order or duplicated change events.",
    ),
    QuestionAnswer(
        slug="idempotent-pipelines",
        category="pipeline-reliability",
        difficulty="medium",
        question="Why do data pipelines need idempotent behavior?",
        short_answer="Because retries, backfills, and replay are normal in data systems, and non-idempotent jobs can duplicate records or corrupt aggregates.",
        deep_dive="A pipeline should be safe to rerun for the same logical input window. That usually means deterministic write paths, merge/upsert semantics, checkpointing, and duplicate suppression. Strong answers mention that idempotency matters not only for failure recovery but also for developer workflows such as reprocessing after schema changes or bug fixes.",
    ),
    QuestionAnswer(
        slug="exactly-once-vs-at-least-once",
        category="pipeline-reliability",
        difficulty="hard",
        question="What is the difference between exactly-once and at-least-once processing?",
        short_answer="At-least-once guarantees no data loss but may duplicate events. Exactly-once aims to ensure each logical event affects results once, typically through stronger coordination or idempotent sinks.",
        deep_dive="Exactly-once is often more about end-to-end semantics than a single framework claim. Many systems achieve practical exactly-once outcomes by combining replayable logs, transactional commits, deterministic state updates, and idempotent sinks. Good answers avoid magic thinking and explain which part of the pipeline really guarantees what.",
    ),
    QuestionAnswer(
        slug="watermarks",
        category="streaming",
        difficulty="hard",
        question="What are watermarks in stream processing?",
        short_answer="Watermarks are progress signals that estimate how complete event-time data is up to a certain point, enabling windowed computations to finalize despite late events.",
        deep_dive="Event-time streams are rarely perfectly ordered. Watermarks let the system trade completeness for timeliness by defining how much lateness it will tolerate before emitting results. Strong answers mention late data handling, allowed lateness, state eviction, and the difference between processing time and event time.",
    ),
    QuestionAnswer(
        slug="checkpointing",
        category="streaming",
        difficulty="medium",
        question="Why is checkpointing important in streaming systems?",
        short_answer="Checkpointing periodically persists state and offsets so a streaming job can recover from failure without recomputing everything from scratch.",
        deep_dive="Stateful stream processing needs a way to restart consistently after failure. Checkpoints tie together operator state and source progress. Good answers mention checkpoint cadence, state backend cost, recovery time, and the fact that checkpointing is often necessary for stronger delivery guarantees.",
    ),
    QuestionAnswer(
        slug="data-quality-dimensions",
        category="data-quality",
        difficulty="easy",
        question="What dimensions of data quality should a pipeline monitor?",
        short_answer="Common dimensions include completeness, accuracy, consistency, freshness, uniqueness, validity, and timeliness.",
        deep_dive="Data quality is broader than schema validity. A pipeline can be technically successful while silently delivering stale, partial, or duplicated data. Good answers talk about row counts, null-rate checks, distribution drift, referential integrity, freshness SLAs, and how failed checks block or quarantine bad datasets.",
    ),
    QuestionAnswer(
        slug="backfills",
        category="operations",
        difficulty="medium",
        question="What is a backfill and what makes it risky?",
        short_answer="A backfill recomputes or reloads historical data, often to correct bugs or onboard new logic. It is risky because it can overwhelm systems, violate idempotency, or change downstream metrics unexpectedly.",
        deep_dive="Backfills are routine in mature data platforms, but they must be designed deliberately. Good answers mention partition-scoped reruns, resource isolation, lineage awareness, write-mode safety, and communication with downstream consumers. A strong candidate explains how to backfill without disrupting current production loads or silently rewriting business history.",
    ),
    QuestionAnswer(
        slug="orchestration-vs-computation",
        category="platform",
        difficulty="medium",
        question="What is the difference between orchestration and computation in data systems?",
        short_answer="Orchestration coordinates when tasks run and how dependencies are managed. Computation engines perform the actual data transformations.",
        deep_dive="Airflow, Dagster, or similar orchestrators schedule tasks, track dependencies, and manage retries, but they are not the execution engine for heavy transformations. Spark, Flink, dbt, warehouses, or SQL engines actually process the data. In interviews, separating these concerns shows platform clarity and avoids designing one tool as if it solves every layer.",
    ),
    QuestionAnswer(
        slug="metadata-lineage",
        category="platform",
        difficulty="medium",
        question="Why do metadata and lineage matter in data engineering?",
        short_answer="They help teams understand where data came from, how it was transformed, who depends on it, and what will break if something changes.",
        deep_dive="Lineage is essential for debugging, impact analysis, compliance, and safe migration. Good answers mention both technical lineage such as job and table dependencies and business metadata such as dataset owners, sensitivity classification, and freshness expectations. Mature platforms treat metadata as infrastructure, not documentation that drifts out of date.",
    ),
    QuestionAnswer(
        slug="warehouse-cost-control",
        category="cost",
        difficulty="medium",
        question="How do data teams control warehouse or lakehouse query cost?",
        short_answer="By pruning scans, modeling data carefully, caching where appropriate, right-sizing compute, limiting wasteful queries, and optimizing file layout.",
        deep_dive="Cost control is often a design question, not a billing afterthought. Practical levers include partition pruning, materialized aggregates, query governance, workload isolation, compaction, and reducing repeated full-history recomputation. Strong answers tie cost control to both storage layout and query discipline.",
    ),
    QuestionAnswer(
        slug="medallion-architecture",
        category="architecture",
        difficulty="easy",
        question="What is a medallion architecture and why do teams use bronze, silver, and gold layers?",
        short_answer="It organizes data maturity stages: bronze for raw landed data, silver for cleaned and standardized data, and gold for curated business-ready outputs.",
        deep_dive="The value of medallion architecture is not the labels themselves but the separation of concerns. Raw ingestion remains replayable, cleaned layers standardize semantics, and curated layers serve analytics or machine learning directly. A strong answer notes that the pattern helps governance, debugging, and recovery because each stage has a distinct purpose.",
    ),
]


def list_categories() -> List[str]:
    return sorted({entry.category for entry in QUESTION_BANK})


def filter_by_category(category: str) -> List[QuestionAnswer]:
    normalized = category.strip().lower()
    return [entry for entry in QUESTION_BANK if entry.category == normalized]


def filter_by_difficulty(difficulty: str) -> List[QuestionAnswer]:
    normalized = difficulty.strip().lower()
    return [entry for entry in QUESTION_BANK if entry.difficulty == normalized]


def search_questions(term: str) -> List[QuestionAnswer]:
    normalized = term.strip().lower()
    if not normalized:
        return QUESTION_BANK[:]
    return [
        entry
        for entry in QUESTION_BANK
        if normalized in entry.question.lower()
        or normalized in entry.short_answer.lower()
        or normalized in entry.deep_dive.lower()
        or normalized in entry.category.lower()
        or normalized in entry.slug.lower()
    ]


def get_question_by_slug(slug: str) -> Optional[QuestionAnswer]:
    normalized = slug.strip().lower()
    for entry in QUESTION_BANK:
        if entry.slug == normalized:
            return entry
    return None


def render_markdown_study_guide() -> str:
    sections = ["# Data Engineering Question Bank", ""]
    for category in list_categories():
        sections.append(f"## {category.replace('-', ' ').title()}")
        sections.append("")
        for entry in filter_by_category(category):
            sections.append(f"### {entry.question}")
            sections.append(f"- Difficulty: `{entry.difficulty}`")
            sections.append(f"- Short answer: {entry.short_answer}")
            sections.append(f"- Deep dive: {entry.deep_dive}")
            sections.append("")
    return "\n".join(sections)
