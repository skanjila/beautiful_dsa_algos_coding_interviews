# Data Engineering Study Guide

This directory is a structured interview-prep module for data engineering.

It includes:

- a typed Python question bank for searching and filtering topics
- a markdown study guide for direct reading
- tests that validate the content structure

## Core Interview Themes

- ingestion and change capture
- batch versus streaming
- data modeling and dimensional design
- reliability and idempotency
- storage layout, partitioning, and file management
- orchestration, lineage, and platform design
- cost and operational tradeoffs

## How To Study

1. Start with fundamentals such as ETL/ELT and batch versus streaming.
2. Move into storage and modeling decisions.
3. Practice pipeline reliability and streaming correctness questions.
4. Rehearse platform and operations topics such as lineage, backfills, and cost control.

## High-Value Questions

### What is the difference between ETL and ELT?

ETL transforms data before loading it into the destination. ELT loads raw data
first and transforms it inside the warehouse or lakehouse.

Deep dive:
The right answer should connect the choice to scaling, reprocessability,
governance, and where compute lives.

### Why does partitioning matter?

Partitioning reduces how much data must be scanned and moved, which improves
query performance and lowers cost when the partition key matches real filters.

Deep dive:
Bad partitioning creates skew and tiny files. Good partitioning follows actual
query patterns such as date, tenant, or region.

### What is change data capture?

CDC incrementally captures inserts, updates, and deletes from a source system
without full reloads.

Deep dive:
A strong answer covers bootstrapping, ordering, delete semantics, duplicates,
and source database impact.

### Why do data pipelines need idempotent behavior?

Because retries, replay, and backfills are normal in production data systems.

Deep dive:
Pipelines should be safe to rerun on the same logical input without creating
duplicate records or double-counted metrics.

### What are watermarks?

Watermarks are progress signals in stream processing that estimate how complete
event-time data is for a given point in time.

Deep dive:
This lets the system close windows while still tolerating late events within a
defined boundary.

## Programmatic Access

```python
from data_engineering.question_bank import search_questions, list_categories

print(list_categories())
for item in search_questions("stream"):
    print(item.question)
```
