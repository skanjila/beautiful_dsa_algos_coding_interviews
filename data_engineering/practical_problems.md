# Data Engineering Practical Interview Problems

This guide focuses on coding-style and design-adjacent data engineering interview
problems. For each problem, the goal is not just to know syntax but to identify
the right pattern quickly and explain it calmly.

## How To Approach These In An Interview

Use this sequence under pressure:

1. Clarify the grain.
   Example: one row per event, one row per user-day, one row per session.
2. Clarify the business key.
   Example: `event_id`, `customer_id`, `(date, user_id)`.
3. Clarify the ordering or tie-break rule.
   Example: latest ingestion timestamp, highest amount, earliest event time.
4. Name the pattern before coding.
   Example: deduplication with windowing, partitioned ranking, sessionization with lag.
5. Explain the Pandas version briefly and the Spark version operationally.
   Pandas shows understanding. Spark shows production-scale thinking.

Good data engineering interviews reward clear semantics first, code second.

## Deduplicate Events

Question:
Given duplicate events, keep the latest record for each `event_id`.

Interview approach:
State the dedup key and the tie-break rule before discussing code.

Pandas approach:
- sort by timestamp
- `drop_duplicates(subset=['event_id'], keep='last')`

Spark approach:
- window partitioned by `event_id`
- order by timestamp descending
- `row_number == 1`

Why this is a common interview pattern:
It tests whether you think in terms of deterministic business rules rather than
just dropping arbitrary duplicates.

## Top N Per Group

Question:
Find the top 3 transactions per customer.

Interview approach:
Say out loud that this is partitioning plus ranking.

Pandas approach:
- sort by `customer_id`, `amount desc`
- `groupby('customer_id').head(3)`

Spark approach:
- window by `customer_id`
- rank or row number by `amount desc`
- filter to top 3

Why this matters:
This is a very common analytics-engineering and Spark SQL pattern.

## Daily Active Users

Question:
Compute DAU from an events table.

Interview approach:
Clarify timezone and valid event types, then say the solution is
"truncate to day, deduplicate users within day, count users per day."

Pandas approach:
- derive date from timestamp
- deduplicate `(date, user_id)`
- group by date and count

Spark approach:
- `to_date` or `date_trunc`
- distinct `(date, user_id)`
- aggregate counts

Why this matters:
This tests metric semantics, not just aggregation syntax.

## Sessionization

Question:
Build user sessions with a 30-minute inactivity threshold.

Interview approach:
Say this is a window-function problem with `lag`, time gap calculation, and cumulative session starts.

Pandas approach:
- sort by user and time
- `shift` previous timestamp
- compute time gap
- flag new sessions
- `cumsum` flags

Spark approach:
- use `lag` over a user/time window
- compute inactivity gap
- cumulative sum of session-start flags

Why this matters:
This tests ordered state transitions and event-time reasoning.

## Slowly Changing Dimension Type 2

Question:
Track customer history without overwriting old values.

Interview approach:
Define business key, tracked columns, effective start/end date, and current-row flag before implementation.

Pandas approach:
- compare incoming rows to active dimension rows
- expire changed current rows
- append new current versions

Spark approach:
- merge/update current rows and insert new versions
- or rewrite affected partitions carefully if merge is unavailable

Why this matters:
This is a standard warehouse modeling interview topic.

## Incremental Aggregation

Question:
Compute hourly aggregates without recomputing all history every run.

Interview approach:
Define the aggregate grain, watermark strategy, and idempotent output key.

Pandas approach:
- filter to new or changed input window
- derive hourly bucket
- aggregate and merge into target

Spark approach:
- read only affected partitions or CDC range
- recompute impacted buckets
- merge or overwrite only impacted output partitions

Why this matters:
It distinguishes full-refresh thinking from production-grade pipeline design.

## Late-Arriving Data

Question:
What do you do when old event-time data arrives after a partition was already processed?

Interview approach:
Define what counts as late, then explain correction policy.

Pandas approach:
- identify impacted historical buckets
- patch or rerun only those windows

Spark approach:
- use watermarks in streaming
- reopen impacted partitions in batch
- route extremely late data through backfill paths

Why this matters:
It tests correctness policy, not just code mechanics.

## Skewed Join

Question:
A Spark join is extremely slow because one key dominates the data. What do you do?

Interview approach:
Start with diagnosis: skewed key distribution, stage stragglers, large shuffle partitions.

Pandas approach:
- profile key frequency
- reason about hot-key isolation or pre-aggregation

Spark approach:
- inspect skew
- consider salting, pre-aggregation, broadcasting, or adaptive skew optimization

Why this matters:
This shows whether you understand distributed performance as a data-shape problem.

## Practical Interview Pattern Map

- duplicates + keep latest -> dedup + ordering
- top N by group -> partition + rank
- daily/weekly actives -> truncate time + distinct + aggregate
- user sessions -> lag + gap detection + cumulative grouping
- dimension history -> compare current state + expire + insert new version
- incremental metrics -> watermark + selective recomputation
- late data -> event-time correction policy
- skewed joins -> distribution diagnosis + targeted mitigation
