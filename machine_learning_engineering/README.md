# Machine Learning Engineering Study Guide

This directory is the repo's dedicated MAANG-oriented machine learning
engineering interview module.

It is intentionally separate from `data_science/` and `system_design/` because
MLE interview loops usually expect you to connect all of the following:

- coding and DSA
- SQL and data reasoning
- ML fundamentals and evaluation
- feature engineering and leakage prevention
- ML system design
- MLOps and production reliability
- product ML domains such as ranking, retrieval, recommendation, and safety
- increasingly, LLM and RAG system reasoning

## What A Strong MLE Study Plan Should Cover

If you want this repo to function as a realistic top-tech MLE prep guide, make
sure you can cover each of these areas without switching mental gears:

1. Coding
   Solve the DSA modules in the main package as if you were interviewing for a
   software-engineering role with ML depth.
2. Data reasoning
   Use `data_engineering/` and the SQL-style thinking there for labels,
   features, and data debugging.
3. ML fundamentals
   Use `data_science/` for modeling, evaluation, leakage, calibration, and
   experimentation.
4. MLE-specific system design
   Use this directory for ranking, recommendation, search, platform, MLOps,
   safety, and LLM-oriented questions.
5. General distributed systems
   Use `system_design/` and `docs/` for service decomposition, scaling,
   reliability, and API design.

## What Is Typically Asked

The most common categories in high-signal MLE loops are:

- coding and data structures
- SQL or feature-building logic
- model debugging and metric selection
- production ML and monitoring
- recommendation, ranking, search, or ads-style design
- experimentation and product tradeoffs
- for some teams, LLM / RAG / evaluation design

## How To Use This Directory

Start with [question_bank.py](question_bank.py) for broad coverage, then move to
[practical_question_bank.py](practical_question_bank.py) for system-style
prompts.

Suggested order:

1. `interview-strategy`
2. `coding`
3. `evaluation`, `feature-engineering`, `modeling`
4. `ml-platform`, `ml-ops`, `reliability-safety`
5. `retrieval-ranking`, `product-ml`, `ml-system-design`
6. `llm-genai` and `company-variants`

## Practical Gap Analysis

Before this module, the repo already had strong material for:

- DSA
- data science fundamentals
- data engineering questions
- general system design

The missing MLE-specific gaps were:

- explicit interview-loop framing
- ranking/recommendation/search-specific question coverage
- platform and training-serving skew questions
- product ML topics like exploration and cold start
- production ML reliability and monitoring as first-class interview themes
- LLM/RAG treated as an MLE systems problem instead of generic AI trivia

This directory fills those gaps.

## Programmatic Access

```python
from machine_learning_engineering.question_bank import list_categories, search_questions

print(list_categories())
for item in search_questions("ranking"):
    print(item.question)
```

## Sources Used To Shape The Coverage

These sources were used to check that the study guide reflects current MLE
interview expectations rather than only generic ML theory:

- Educative overview of ML system design interviews:
  https://www.educative.io/blog/how-to-crack-machine-learning-system-design-interview
- Educative ML interview course overview:
  https://www.educative.io/courses/grokking-the-machine-learning-interview
- Educative ML system design framework overview:
  https://www.educative.io/courses/machine-learning-system-design/introduction
- Apple Applied ML / search-oriented job descriptions, which emphasize search,
  ranking, evaluation, low-latency inference, and production ML:
  https://jobs.apple.com/en-us/details/200613991/aiml-sr-machine-learning-engineer-answers-knowledge-information-aki
  https://jobs.apple.com/en-us/details/200601758-3401/aiml-staff-machine-learning-engineer-search-quality-answers-knowledge-information-aki
  https://jobs.apple.com/en-us/details/200612079/aiml-staff-machine-learning-engineer-answers-knowledge-intelligence
