# Data Engineering Interview Walkthrough

## Default Answer Structure

1. Clarify the business goal.
2. Clarify data sources and freshness requirements.
3. Estimate data volume, event rate, and retention.
4. Describe ingestion.
5. Describe storage layout and modeling.
6. Describe transformation and serving layers.
7. Add quality checks, replay strategy, and failure handling.
8. Close with cost and operational tradeoffs.

## Questions To Ask Early

- Is this batch, streaming, or hybrid?
- What is the expected freshness SLA?
- What is the data volume and skew pattern?
- Do we need history or only current state?
- Are updates and deletes present?
- Who consumes the result: analysts, ML systems, APIs, or dashboards?
- What correctness guarantees matter most?

## Common Follow-Ups

### How would you handle schema changes?

Use versioned contracts, backward-compatible additions where possible, schema
validation, and rollout processes that protect downstream consumers.

### How would you reprocess historical data safely?

Use partition-scoped backfills, idempotent writes, staging or shadow outputs,
and impact-aware communication with downstream owners.

### How would you monitor the pipeline?

Track freshness, row counts, null rates, duplicates, task success, cost, lag,
and downstream dataset health.
