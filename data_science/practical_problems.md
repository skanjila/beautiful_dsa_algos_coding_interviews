# Data Science Practical Python Solutions

This guide adds executable-style Python solution patterns to common practical
data-science interview problems.

## How To Approach These In Interviews

Use this structure:

1. Define the prediction target and what is known at prediction time.
2. State the feature-engineering or evaluation risk.
   Example: leakage, imbalance, drift, time order.
3. Give a Pandas approach for data handling.
4. Give a scikit-learn or Python ML approach for modeling.

That communicates both practical fluency and modeling judgment.

## Mixed-Type Preprocessing Pipeline

### Pandas

```python
numeric_cols = ["age", "income", "tenure_days"]
categorical_cols = ["country", "device_type", "segment"]

X = df[numeric_cols + categorical_cols].copy()
y = df["target"].copy()
```

### Python / scikit-learn

```python
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression


numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("one_hot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numeric_cols),
        ("cat", categorical_pipeline, categorical_cols),
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)
```

Interview note:
- say "preprocessing belongs inside the pipeline" to show leakage awareness

## Leakage-Safe Time Window Features

### Pandas

```python
import pandas as pd


def build_user_spend_last_7_days(df: pd.DataFrame) -> pd.DataFrame:
    frame = df.sort_values(["user_id", "event_ts"]).copy()
    frame["event_ts"] = pd.to_datetime(frame["event_ts"], utc=True)
    frame["amount_lagged"] = frame.groupby("user_id")["amount"].shift(1)
    frame["rolling_7d_spend"] = (
        frame.groupby("user_id")
             .apply(
                 lambda group: group.set_index("event_ts")["amount_lagged"]
                 .rolling("7D", min_periods=1)
                 .sum()
                 .reset_index(drop=True)
             )
             .reset_index(level=0, drop=True)
    )
    return frame
```

### Python / ML workflow

```python
# The modeling pipeline comes after the feature table is built.
# The interview-critical point is that the feature uses only prior rows.
```

Interview note:
- always define the prediction timestamp before describing the feature logic

## Baseline Binary Classifier

### Pandas

```python
X = df.drop(columns=["target"])
y = df["target"]
```

### Python / scikit-learn

```python
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model.fit(X_train, y_train)
preds = model.predict(X_test)
probs = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, preds))
print("ROC AUC:", roc_auc_score(y_test, probs))
```

Interview note:
- start with a baseline before suggesting a more complex model

## Imbalanced Classification

### Python / scikit-learn

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, average_precision_score


model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train, y_train)
scores = model.predict_proba(X_valid)[:, 1]

precision, recall, thresholds = precision_recall_curve(y_valid, scores)
pr_auc = average_precision_score(y_valid, scores)
print("PR AUC:", pr_auc)
```

Interview note:
- mention threshold tuning, not just class weighting

## Feature Importance Workflow

### Python / scikit-learn

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance


forest = RandomForestClassifier(random_state=42)
forest.fit(X_train, y_train)

importance = permutation_importance(forest, X_valid, y_valid, n_repeats=5, random_state=42)
```

Interview note:
- explain why permutation importance is often more trustworthy than raw tree impurity importance

## Time Series Validation

### Python / scikit-learn

```python
from sklearn.model_selection import TimeSeriesSplit


tscv = TimeSeriesSplit(n_splits=5)

for train_idx, valid_idx in tscv.split(X):
    X_train, X_valid = X.iloc[train_idx], X.iloc[valid_idx]
    y_train, y_valid = y.iloc[train_idx], y.iloc[valid_idx]
    model.fit(X_train, y_train)
```

Interview note:
- say why random splits are wrong before showing the tool

## Text Baseline

### Python / scikit-learn

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


text_model = Pipeline(
    steps=[
        ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)
```

Interview note:
- sparse text baseline + linear model is often the strongest calm answer
