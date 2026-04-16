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
    python_ml_approach: str
    deep_dive: str


PRACTICAL_QUESTION_BANK: List[PracticalQuestion] = [
    PracticalQuestion(
        slug="build-preprocessing-pipeline",
        category="feature-engineering",
        difficulty="medium",
        question="How would you build a preprocessing pipeline for mixed numeric and categorical tabular features?",
        interview_approach="Start by separating feature types, then say you want transformations that are fit only on training data and applied consistently at inference time. Mention leakage-safe pipelines before naming any library.",
        pandas_approach="Use Pandas to inspect dtypes, missingness, and cardinality, then explicitly define numeric and categorical column lists. Pandas is great for feature profiling and sanity checks before the final modeling pipeline is built.",
        python_ml_approach="Use `ColumnTransformer` with numeric imputation and scaling plus categorical imputation and one-hot encoding inside a `Pipeline`. This is the clean scikit-learn answer because it keeps preprocessing tied to the model and reduces leakage risk.",
        deep_dive="Interviewers want to hear that preprocessing belongs inside the trainable pipeline, not in a notebook cell that mutates the full dataset before splitting. A strong answer also mentions unknown categories at inference time and reproducibility of the preprocessing graph.",
    ),
    PracticalQuestion(
        slug="time-window-features",
        category="feature-engineering",
        difficulty="hard",
        question="How would you create rolling 7-day user features without leakage?",
        interview_approach="Define the prediction timestamp first. Then say all features must use only records strictly earlier than that timestamp. The core pattern is grouped lagged aggregation, not arbitrary rolling over the full table.",
        pandas_approach="Sort by entity and timestamp, use `groupby` with `rolling` or cumulative aggregates on prior rows only, and align results back to the original rows. The important point is ensuring the current row is excluded from its own historical feature.",
        python_ml_approach="The modeling side is usually secondary here; the key Python answer is the feature-construction function itself. Once features are constructed leakage-safely, they can feed a downstream scikit-learn pipeline.",
        deep_dive="This is one of the most realistic data-science interview questions because it bridges feature engineering and data correctness. Strong answers mention point-in-time joins, lagging, validation by chronology, and how to reproduce the same logic in production feature pipelines.",
    ),
    PracticalQuestion(
        slug="baseline-classifier",
        category="modeling",
        difficulty="easy",
        question="How would you build a simple baseline binary classifier in Python?",
        interview_approach="Name the baseline before optimizing. A logistic regression or small tree-based model is usually enough to establish whether the problem is learnable and whether the features carry signal.",
        pandas_approach="Use Pandas to define `X` and `y`, inspect class balance, and split data carefully. Pandas is mostly the data-handling layer here, not the model-training layer.",
        python_ml_approach="Use `train_test_split`, build a preprocessing `Pipeline`, train a `LogisticRegression`, and report metrics such as precision, recall, ROC AUC, or PR AUC depending on the business context.",
        deep_dive="Good candidates do not jump straight to complex models. They establish a baseline, measure it, and only then justify more complexity. In interviews, that usually signals better judgment than immediately naming XGBoost or neural nets.",
    ),
    PracticalQuestion(
        slug="class-imbalance-model",
        category="modeling",
        difficulty="medium",
        question="How would you train and evaluate a classifier on an imbalanced dataset?",
        interview_approach="State that metric choice comes before model choice. Then explain whether recall, precision, PR AUC, or threshold tuning matters most for the business objective.",
        pandas_approach="Use Pandas to quantify imbalance, inspect positive counts, and perhaps stratify splits correctly. This helps avoid reporting misleading accuracy on a skewed dataset.",
        python_ml_approach="Use a baseline classifier with `class_weight='balanced'` or sampling logic, evaluate with precision-recall metrics, and tune the decision threshold rather than relying on the default 0.5 cut. Mention calibration if predicted probabilities are used operationally.",
        deep_dive="Interviewers often look for whether you understand that handling imbalance is not just about resampling. The best answers connect thresholding, business cost, metric selection, and label prevalence.",
    ),
    PracticalQuestion(
        slug="feature-importance-workflow",
        category="interpretability",
        difficulty="medium",
        question="How would you explain which features matter in a trained tabular model?",
        interview_approach="First ask whether the audience needs global explanation, local explanation, or both. Then explain that the method depends on model type and whether stability matters more than raw convenience.",
        pandas_approach="Use Pandas to align feature names with coefficients or importance values and produce sorted explanation tables. Pandas is often how you make model outputs readable for humans.",
        python_ml_approach="For linear models, inspect standardized coefficients carefully. For tree ensembles, use built-in feature importances as a first pass and permutation importance or SHAP-style explanations for deeper analysis. Mention caveats like correlation and instability.",
        deep_dive="This question tests communication as much as modeling. Strong answers avoid overselling a single importance number and mention correlated features, local versus global explanation, and stakeholder-friendly framing.",
    ),
    PracticalQuestion(
        slug="time-series-validation",
        category="evaluation",
        difficulty="medium",
        question="How would you evaluate a forecasting or time-dependent prediction problem in Python?",
        interview_approach="Say immediately that random train-test splits are unsafe when time order matters. Then describe a chronological split, rolling validation, or expanding-window evaluation.",
        pandas_approach="Use Pandas to sort by time, create cut points, and generate explicit train/validation slices that mimic the production forecast horizon.",
        python_ml_approach="Use `TimeSeriesSplit` when appropriate, or hand-built rolling windows if the forecast setup is more specialized. Evaluate with the metric that matches the business question, such as MAE, RMSE, MAPE, or directional accuracy.",
        deep_dive="The key signal is whether your evaluation matches the deployment setting. Strong answers mention forecast horizon, seasonality, concept drift, and that validation must simulate predicting the future from the past.",
    ),
    PracticalQuestion(
        slug="text-baseline",
        category="feature-engineering",
        difficulty="medium",
        question="How would you build a baseline text classification model in Python?",
        interview_approach="Say that the baseline is usually sparse text features plus a simple linear model. This shows you know how to get signal quickly before jumping into large language or transformer models.",
        pandas_approach="Use Pandas to clean labels, inspect class counts, and manage the train-validation split. Text columns often need simple normalization and basic sanity checks first.",
        python_ml_approach="Use `TfidfVectorizer` inside a scikit-learn pipeline with logistic regression or linear SVM. Evaluate with task-appropriate metrics and inspect the most informative tokens for sanity.",
        deep_dive="This is a high-value interview answer because it is practical and credible. Strong candidates mention leakage in text-derived metadata, tokenization choices, and why a sparse linear baseline is still a strong first step.",
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
        or normalized in entry.python_ml_approach.lower()
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
    sections = ["# Data Science Practical Interview Problems", ""]
    for category in list_categories():
        sections.append(f"## {category.replace('-', ' ').title()}")
        sections.append("")
        for entry in filter_by_category(category):
            sections.append(f"### {entry.question}")
            sections.append(f"- Difficulty: `{entry.difficulty}`")
            sections.append(f"- Interview approach: {entry.interview_approach}")
            sections.append(f"- Pandas approach: {entry.pandas_approach}")
            sections.append(f"- Python/ML approach: {entry.python_ml_approach}")
            sections.append(f"- Deep dive: {entry.deep_dive}")
            sections.append("")
    return "\n".join(sections)
