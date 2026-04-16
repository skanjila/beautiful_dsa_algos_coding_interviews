# Machine Learning Engineering Practice Problems

This file is the contribution backlog for MLE and LLM-oriented practice work.

The goal is simple:

- keep a visible list of missing or intentionally stubbed problems
- make it easy to contribute one focused implementation at a time
- separate runnable reference helpers from deliberate practice exercises

## How To Use This

If you want to contribute:

1. Pick one stubbed function from [practice_stubs.py](practice_stubs.py).
2. Read the matching metadata entry in [practice_problems.py](practice_problems.py).
3. Implement the function.
4. Add tests for the expected behavior.
5. Update the `status` from `stubbed` to `implemented`.

## Current Backlog

### Evaluation

- `compute_average_precision`
- `compute_brier_score`

### Feature Engineering / ML Platform

- `detect_feature_freshness_gaps`
- `build_point_in_time_dataset_index`

### Modeling / Ranking

- `compute_auc_from_pairs`
- `rerank_by_business_rules`
- `sample_hard_negatives`
- `simulate_bandit_exploration`
- `select_review_threshold`

### LLM / GenAI

- `map_documents_to_chunks`
- `score_rag_answer_groundedness`
- `build_retrieval_eval_report`

## What Already Has Runnable Code

See [solutions.py](solutions.py) for working helpers and examples for:

- precision and recall at k
- DCG and NDCG
- calibration buckets and expected calibration error
- population stability index
- chunking for simple RAG flows
- keyword retrieval baselines
- reciprocal rank fusion
- citation coverage scoring
