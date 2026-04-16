# Data Science Study Guide

This directory is a structured interview-prep module for data science.

It includes:

- a typed Python question bank
- a readable markdown study guide
- tests that verify the content structure and helper functions

## Core Interview Themes

- modeling fundamentals
- evaluation and metric selection
- preprocessing and feature design
- feature engineering and leakage-safe feature construction
- experimentation and causal reasoning
- model reliability and production monitoring
- communication and business framing

## How To Study

1. Start with fundamentals like bias-variance and overfitting.
2. Move into evaluation metrics and validation strategy.
3. Practice practical topics like feature engineering, leakage, missing values, class imbalance, and SQL.
4. Rehearse how to connect model choices to business outcomes.

## High-Value Questions

### What is the bias-variance tradeoff?

Bias is error from overly simple assumptions. Variance is error from
over-sensitivity to training data noise. Good models balance both.

Deep dive:
Great answers connect bias and variance to training versus validation behavior
and explain what to do when each problem dominates.

### Why do we use precision and recall instead of accuracy sometimes?

Because accuracy hides failure modes when the classes are imbalanced or when the
costs of false positives and false negatives are very different.

Deep dive:
The best answer ties metric choice to the decision context, not just textbook
definitions.

### What is feature leakage?

Feature leakage is information in training data that would not really be
available at prediction time.

Deep dive:
Leakage produces unrealistically strong validation metrics and is often caused
by poor pipeline design rather than the model itself.

### How would you build time-window features without leakage?

Use only data available before the prediction timestamp, often through lagged
windows and point-in-time joins.

Deep dive:
This is one of the most common practical feature-engineering interview questions
because it tests whether you understand modeling and data pipeline correctness
together.

### How do you choose categorical encodings?

The answer depends on model type, cardinality, and leakage risk.

Deep dive:
One-hot encoding is often the default for low-cardinality safe features. Target
encoding can be useful but requires leakage-safe computation. High-cardinality
features need more careful tradeoff analysis.

### What is concept drift?

Concept drift means the relationship between inputs and target changes over
time, causing old models to degrade.

Deep dive:
A good answer distinguishes data drift from concept drift and explains how to
monitor and respond operationally.

### Why must data scientists think in business metrics?

Because model metrics are only useful if they improve the real product or
business outcome the model is meant to support.

## Programmatic Access

```python
from data_science.question_bank import search_questions, list_categories

print(list_categories())
for item in search_questions("metric"):
    print(item.question)
```
