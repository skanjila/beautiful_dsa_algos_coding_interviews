# Data Science Interview Walkthrough

## Default Answer Structure

1. Clarify the business objective.
2. Clarify the prediction target and data available at decision time.
3. Define success metrics.
4. Describe validation strategy.
5. Choose a baseline model.
6. Discuss feature engineering and preprocessing.
7. Discuss failure modes such as leakage, drift, or imbalance.
8. Close with deployment, monitoring, and business tradeoffs.

## Questions To Ask Early

- What is the exact prediction or decision problem?
- What does success look like in business terms?
- How imbalanced is the data?
- Are labels delayed or noisy?
- Is this a static tabular problem, time series, ranking, or causal question?
- What information is available at prediction time?
- How will the model be consumed in production?

## Common Follow-Ups

### What baseline would you start with?

Start with the simplest strong baseline that matches the data type, such as
logistic regression for classification, linear regression for regression, or a
tree ensemble for strong tabular performance.

### How would you detect leakage?

Trace every feature back to what timestamp or process produced it and ask
whether it would really exist at prediction time.

### How would you monitor the model after launch?

Track latency, error rate, input drift, prediction distribution changes,
business KPI movement, and delayed label-based quality when labels arrive.
