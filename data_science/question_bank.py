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
        slug="bias-variance-tradeoff",
        category="fundamentals",
        difficulty="easy",
        question="What is the bias-variance tradeoff?",
        short_answer="Bias is error from overly simple assumptions, while variance is error from sensitivity to training data noise. Good models balance both.",
        deep_dive="High-bias models underfit because they cannot capture the real signal. High-variance models overfit because they chase noise in the training set. Strong interview answers explain how training error and validation error move under each regime and mention techniques like regularization, feature simplification, or more data depending on the failure mode.",
    ),
    QuestionAnswer(
        slug="underfitting-vs-overfitting",
        category="fundamentals",
        difficulty="easy",
        question="What is the difference between underfitting and overfitting?",
        short_answer="Underfitting means the model performs poorly on both training and validation data. Overfitting means it performs well on training data but poorly on unseen data.",
        deep_dive="This question is often a setup for discussing diagnostic behavior. Underfitting suggests insufficient model capacity, poor features, or too much regularization. Overfitting suggests excessive model complexity, leakage, or insufficient data. Good answers mention validation curves and generalization, not just memorized definitions.",
    ),
    QuestionAnswer(
        slug="train-validation-test",
        category="fundamentals",
        difficulty="easy",
        question="Why do we split data into train, validation, and test sets?",
        short_answer="Training data fits the model, validation data guides model selection and tuning, and the test set estimates final generalization performance.",
        deep_dive="Without a clean separation, model selection can leak information and produce optimistic metrics. The validation set is for iteration; the test set should remain untouched until final evaluation. Strong answers mention stratification, temporal splits when appropriate, and the danger of repeatedly peeking at the test set.",
    ),
    QuestionAnswer(
        slug="precision-recall",
        category="evaluation",
        difficulty="easy",
        question="What is the difference between precision and recall?",
        short_answer="Precision measures how many predicted positives are truly positive. Recall measures how many true positives were successfully found.",
        deep_dive="The right metric depends on the cost of false positives and false negatives. High precision matters when false alarms are expensive. High recall matters when missing positives is costly. Good answers discuss threshold tuning and domain tradeoffs such as fraud detection, medical screening, or content moderation.",
    ),
    QuestionAnswer(
        slug="roc-vs-pr",
        category="evaluation",
        difficulty="medium",
        question="When is a precision-recall curve more informative than an ROC curve?",
        short_answer="Precision-recall curves are usually more informative on highly imbalanced datasets because they focus on positive-class performance.",
        deep_dive="ROC curves can look deceptively strong when the negative class dominates because false positive rate stays numerically small. Precision-recall curves surface the actual quality of positive predictions more directly. Strong answers connect the metric choice to base rate, decision thresholding, and business cost.",
    ),
    QuestionAnswer(
        slug="cross-validation",
        category="evaluation",
        difficulty="medium",
        question="Why do we use cross-validation?",
        short_answer="Cross-validation reduces dependence on a single split and provides a more stable estimate of model performance, especially when data is limited.",
        deep_dive="K-fold cross-validation rotates which subset acts as validation data so more of the dataset contributes to evaluation. It is useful when you need robust model comparison under limited sample size. Good answers also note when not to use naive cross-validation, such as time series, grouped entities, or leakage-prone repeated observations.",
    ),
    QuestionAnswer(
        slug="feature-scaling",
        category="preprocessing",
        difficulty="easy",
        question="Why does feature scaling matter for some models?",
        short_answer="Models based on distance, gradients, or regularized linear coefficients can behave poorly when features are on wildly different scales.",
        deep_dive="KNN, k-means, SVMs with certain kernels, logistic regression with regularization, and neural networks are all sensitive to scale in different ways. Tree-based models are usually much less sensitive. Strong answers mention standardization versus normalization and tie preprocessing to the model family rather than treating scaling as universal.",
    ),
    QuestionAnswer(
        slug="missing-values",
        category="preprocessing",
        difficulty="medium",
        question="How should you handle missing values?",
        short_answer="The right approach depends on why values are missing and how the model uses them. Common strategies include imputation, missing indicators, row filtering, or model classes that can handle missingness directly.",
        deep_dive="The most important step is understanding the missingness mechanism: MCAR, MAR, or MNAR. Blindly imputing can distort signal or hide a meaningful absence pattern. Good answers mention simple imputations, model-based imputations, missing flags, leakage risks, and how the business meaning of missingness can itself be predictive.",
    ),
    QuestionAnswer(
        slug="categorical-encoding",
        category="feature-engineering",
        difficulty="medium",
        question="How do you choose between one-hot encoding, ordinal encoding, target encoding, and learned embeddings for categorical features?",
        short_answer="The choice depends on cardinality, model family, leakage risk, and whether category order has real meaning. One-hot is safe for low cardinality, target encoding is compact but leakage-prone, and embeddings are useful in richer learned models.",
        deep_dive="Feature encoding is not just a preprocessing checkbox. One-hot encoding works well for linear models and trees when the number of categories is manageable. Ordinal encoding is only valid when order is real, not arbitrary. Target encoding can be powerful for high-cardinality features but must be done with careful cross-validation or out-of-fold computation to avoid leakage. Embeddings are useful when the model can learn dense representations and when interactions are too rich for manual sparse encoding.",
    ),
    QuestionAnswer(
        slug="feature-crosses",
        category="feature-engineering",
        difficulty="medium",
        question="When are interaction features or feature crosses useful?",
        short_answer="They are useful when the relationship between variables depends on combinations rather than individual features alone, especially in linear models that cannot discover nonlinear interactions by themselves.",
        deep_dive="Feature crosses let simple models represent richer decision boundaries. For example, location and device type may be weak on their own but predictive together. Strong interview answers mention that tree models often capture interactions automatically, while linear models may need explicit interaction terms. Also note that too many crosses can explode dimensionality and overfit unless guided by domain knowledge or regularization.",
    ),
    QuestionAnswer(
        slug="time-window-features",
        category="feature-engineering",
        difficulty="hard",
        question="How would you build rolling or time-window features without causing leakage?",
        short_answer="Compute features using only data available before the prediction timestamp, often with lagged windows, grouped rolling aggregates, and strict point-in-time joins.",
        deep_dive="This is one of the most common practical interview questions because it separates modeling knowledge from real production judgment. A strong answer mentions defining a prediction timestamp, restricting aggregations to prior data only, and avoiding joins that accidentally include future information. Good examples include rolling 7-day spend, prior session count, or historical conversion rate up to but excluding the current event.",
    ),
    QuestionAnswer(
        slug="high-cardinality-features",
        category="feature-engineering",
        difficulty="medium",
        question="How do you handle high-cardinality categorical features such as user IDs, URLs, or product SKUs?",
        short_answer="Options include hashing, target encoding, learned embeddings, grouping rare categories, or using models that can leverage such identifiers carefully.",
        deep_dive="High-cardinality features can be powerful but dangerous. They may capture identity-level signal or pure memorization. Good answers mention separating long-tail categories, avoiding huge sparse expansions when one-hot would be impractical, and using leakage-safe encodings. A strong candidate also discusses whether the feature will generalize to unseen categories and whether it represents stable behavior or noisy memorization.",
    ),
    QuestionAnswer(
        slug="feature-normalization-choice",
        category="feature-engineering",
        difficulty="easy",
        question="How do you decide whether to standardize, normalize, log-transform, or leave a numeric feature unchanged?",
        short_answer="It depends on the feature distribution, the model family, and whether large magnitudes or heavy skew would distort optimization or interpretation.",
        deep_dive="Standardization is common when models depend on scale-sensitive optimization or regularization. Normalization can matter for distance-based methods. Log transforms are useful for positive, highly skewed variables such as counts or revenue. Good answers mention outliers, zero handling, train-only fitting of transformation statistics, and that tree models usually need less scaling work than linear models or neural networks.",
    ),
    QuestionAnswer(
        slug="aggregated-features",
        category="feature-engineering",
        difficulty="medium",
        question="How do you create aggregated historical features such as user average spend or merchant fraud rate safely?",
        short_answer="Compute them over historical data only, keyed by the appropriate entity, and ensure the aggregation respects training-validation boundaries to avoid leakage.",
        deep_dive="Aggregated features are high-value but also high-risk. The main danger is accidentally including the current label or future records when computing historical statistics. Strong answers mention point-in-time correctness, entity keys, lagged aggregation windows, minimum-support thresholds for noisy entities, and fallback values for cold-start cases.",
    ),
    QuestionAnswer(
        slug="text-feature-engineering",
        category="feature-engineering",
        difficulty="medium",
        question="How would you engineer features from raw text for a traditional machine learning interview problem?",
        short_answer="Common approaches include tokenization, lowercasing, stop-word handling, n-grams, TF-IDF, and possibly hand-crafted metadata such as length or punctuation counts.",
        deep_dive="Even when deep language models exist, interviews often still probe whether you can reason from first principles. A strong answer explains preprocessing decisions, sparse vectorization, and when metadata features are useful. Good candidates also mention leakage through text fields that accidentally contain labels, such as moderation reasons or manually assigned tags.",
    ),
    QuestionAnswer(
        slug="class-imbalance",
        category="modeling",
        difficulty="medium",
        question="How do you handle class imbalance?",
        short_answer="Possible approaches include resampling, class weighting, threshold tuning, alternative metrics, anomaly framing, or collecting more positive examples.",
        deep_dive="Class imbalance is not solved by one trick. Oversampling can help recall but may overfit; undersampling can lose information; class weighting changes the optimization objective; threshold tuning changes operating behavior. Strong answers start with metric choice and business cost before choosing technical interventions.",
    ),
    QuestionAnswer(
        slug="regularization",
        category="modeling",
        difficulty="medium",
        question="What problem does regularization solve?",
        short_answer="Regularization discourages overly complex models so they generalize better instead of fitting noise.",
        deep_dive="L1 encourages sparsity, while L2 shrinks coefficients smoothly. In neural networks, regularization also appears as dropout, weight decay, early stopping, and augmentation. Strong answers connect regularization to variance reduction and explain how too much regularization can push the model back into underfitting.",
    ),
    QuestionAnswer(
        slug="linear-vs-tree-models",
        category="model-selection",
        difficulty="medium",
        question="How do you think about choosing between linear models and tree-based models?",
        short_answer="Linear models are simple, interpretable, and effective when relationships are mostly additive and well-engineered. Tree models capture nonlinear interactions with less feature engineering.",
        deep_dive="The right choice depends on data size, feature representation, interpretability needs, and inference constraints. Linear models can be strong baselines and are often easier to debug. Tree ensembles perform well on tabular data with mixed nonlinear effects. Good answers compare them in terms of feature scaling, missingness, calibration, and operational cost.",
    ),
    QuestionAnswer(
        slug="feature-leakage",
        category="reliability",
        difficulty="medium",
        question="What is feature leakage?",
        short_answer="Feature leakage occurs when training data contains information that would not actually be available at prediction time, causing overly optimistic performance.",
        deep_dive="Leakage can come from future information, target-derived columns, aggregation windows that peek ahead, or preprocessing fit on the full dataset before splitting. Strong answers emphasize that leakage is a pipeline-design problem as much as a modeling problem, and they explain how to detect it through timeline thinking and suspiciously high validation metrics.",
    ),
    QuestionAnswer(
        slug="calibration",
        category="evaluation",
        difficulty="hard",
        question="What does calibration mean for a probabilistic classifier?",
        short_answer="Calibration measures whether predicted probabilities match empirical outcome frequencies, not just whether class rankings are good.",
        deep_dive="A model can rank examples well yet still produce unusable probabilities. Calibration matters for threshold setting, risk scoring, and downstream decision systems. Strong answers mention reliability curves, Brier score, Platt scaling, isotonic regression, and the difference between discrimination and probability quality.",
    ),
    QuestionAnswer(
        slug="causal-vs-predictive",
        category="experimentation",
        difficulty="medium",
        question="What is the difference between predictive modeling and causal inference?",
        short_answer="Predictive modeling estimates what is likely to happen. Causal inference estimates what would happen under an intervention.",
        deep_dive="This distinction matters because high predictive accuracy does not imply valid treatment-effect estimation. Confounding, selection bias, and counterfactual reasoning are central in causal work but not necessarily in standard supervised prediction. Strong answers mention randomized experiments, observational adjustment, and why the objective must be clear before choosing methods.",
    ),
    QuestionAnswer(
        slug="ab-testing",
        category="experimentation",
        difficulty="medium",
        question="What are common pitfalls in A/B testing?",
        short_answer="Pitfalls include peeking too early, underpowered tests, multiple comparisons, bad randomization, metric mismatch, novelty effects, and interference between users.",
        deep_dive="A/B testing looks simple but breaks easily in practice. Strong answers mention predefining metrics, sample-size reasoning, guardrail metrics, segmentation traps, and operational issues like exposure logging. Good candidates also discuss whether the chosen success metric actually aligns with the business outcome being optimized.",
    ),
    QuestionAnswer(
        slug="time-series-validation",
        category="evaluation",
        difficulty="medium",
        question="Why can't you always use random train-test splits for time series?",
        short_answer="Random splits can leak future information into training. Time series require chronological validation that respects temporal ordering.",
        deep_dive="Time-dependent data changes the evaluation protocol because deployment always predicts the future from the past. Strong answers mention rolling windows, expanding windows, seasonality, concept drift, and forecast horizon. The key point is that validation must simulate the real prediction setting.",
    ),
    QuestionAnswer(
        slug="concept-drift",
        category="ml-ops",
        difficulty="medium",
        question="What is concept drift and why does it matter?",
        short_answer="Concept drift means the relationship between inputs and target changes over time, causing model performance to decay if the model is not updated or monitored.",
        deep_dive="Concept drift can appear as changes in feature distribution, target prevalence, or label generation process. Good answers distinguish between data drift and true concept drift and mention monitoring strategies, retraining policy, shadow evaluation, and alert thresholds tied to business risk.",
    ),
    QuestionAnswer(
        slug="model-monitoring",
        category="ml-ops",
        difficulty="medium",
        question="What should a production model-monitoring system track?",
        short_answer="It should track input distributions, prediction distributions, latency, failure rate, business outcomes, and when available, delayed label-based performance metrics.",
        deep_dive="Monitoring is not only about p99 latency. You also need to know whether the model is receiving valid inputs, whether prediction scores drift, whether thresholds still make sense, and whether the business KPI is degrading. Strong answers mention offline-online skew, feature freshness, shadow deployments, and delayed feedback loops.",
    ),
    QuestionAnswer(
        slug="interpretability",
        category="communication",
        difficulty="medium",
        question="How do you explain a complex model to non-technical stakeholders?",
        short_answer="Focus on the business question, the decision the model supports, the major drivers, the known limitations, and how performance is measured in human terms.",
        deep_dive="Interpretability is partly a communication exercise. Stakeholders rarely need raw mathematical detail first; they need to know what the model is for, why it can be trusted within limits, and what failure modes exist. Good answers mention feature importance, local explanations, calibration, fairness considerations, and plain-language metric framing.",
    ),
    QuestionAnswer(
        slug="sql-in-data-science",
        category="practical",
        difficulty="easy",
        question="Why is SQL important for data science interviews?",
        short_answer="Because much of real-world data science starts with extracting, joining, aggregating, validating, and exploring data in relational systems.",
        deep_dive="Many interview loops use SQL to evaluate whether a candidate can reason about data shape before modeling. Strong answers note that SQL is not separate from data science; it is part of feature preparation, cohort analysis, experiment analysis, and data validation. Candidates who can only talk model theory often struggle in practical roles.",
    ),
    QuestionAnswer(
        slug="business-metrics",
        category="communication",
        difficulty="easy",
        question="Why do data scientists need to think in business metrics instead of only model metrics?",
        short_answer="Because a technically strong model can still fail if it does not improve the actual business decision or user outcome it was built to support.",
        deep_dive="Accuracy, AUC, and RMSE are not the product objective. Good answers tie modeling work to revenue, retention, conversion, fraud loss, support cost, or user trust. Strong candidates show they can bridge technical optimization and business value, especially when discussing threshold decisions or experimentation.",
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
    sections = ["# Data Science Question Bank", ""]
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
