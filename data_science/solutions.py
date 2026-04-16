from __future__ import annotations

import math
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Iterable, List, Sequence


Row = Dict[str, Any]


def _parse_timestamp(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    if isinstance(value, str):
        normalized = value.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(normalized)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    raise TypeError(f"Unsupported timestamp value: {value!r}")


def infer_feature_types(rows: Sequence[Row], target_field: str) -> Dict[str, List[str]]:
    """Split columns into numeric and categorical groups using observed values."""
    feature_names = [key for key in rows[0].keys() if key != target_field]
    numeric: List[str] = []
    categorical: List[str] = []

    for feature in feature_names:
        values = [row.get(feature) for row in rows if row.get(feature) is not None]
        if values and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in values):
            numeric.append(feature)
        else:
            categorical.append(feature)

    return {"numeric": numeric, "categorical": categorical}


def build_preprocessing_plan(rows: Sequence[Row], target_field: str) -> Dict[str, Any]:
    """Compute imputation and scaling statistics for tabular features."""
    feature_types = infer_feature_types(rows, target_field)
    numeric_stats: Dict[str, Dict[str, float]] = {}
    categorical_defaults: Dict[str, str] = {}
    categorical_values: Dict[str, List[str]] = {}

    for feature in feature_types["numeric"]:
        values = [float(row[feature]) for row in rows if row.get(feature) is not None]
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        numeric_stats[feature] = {
            "mean": mean,
            "std": math.sqrt(variance) or 1.0,
            "impute": mean,
        }

    for feature in feature_types["categorical"]:
        observed = [str(row[feature]) for row in rows if row.get(feature) is not None]
        mode = Counter(observed).most_common(1)[0][0] if observed else "missing"
        categorical_defaults[feature] = mode
        categorical_values[feature] = sorted(set(observed + [mode]))

    return {
        "numeric": feature_types["numeric"],
        "categorical": feature_types["categorical"],
        "numeric_stats": numeric_stats,
        "categorical_defaults": categorical_defaults,
        "categorical_values": categorical_values,
    }


def preprocess_rows(
    rows: Sequence[Row],
    target_field: str,
    plan: Dict[str, Any],
) -> tuple[List[List[float]], List[int], List[str]]:
    """Impute, scale, and one-hot encode rows into a model-ready matrix."""
    feature_names: List[str] = []
    for feature in plan["numeric"]:
        feature_names.append(feature)
    for feature in plan["categorical"]:
        for category in plan["categorical_values"][feature]:
            feature_names.append(f"{feature}={category}")

    matrix: List[List[float]] = []
    labels: List[int] = []

    for row in rows:
        features: List[float] = []
        for feature in plan["numeric"]:
            stats = plan["numeric_stats"][feature]
            value = float(row.get(feature, stats["impute"]) if row.get(feature) is not None else stats["impute"])
            features.append((value - stats["mean"]) / stats["std"])

        for feature in plan["categorical"]:
            current = str(
                row.get(feature, plan["categorical_defaults"][feature])
                if row.get(feature) is not None
                else plan["categorical_defaults"][feature]
            )
            for category in plan["categorical_values"][feature]:
                features.append(1.0 if current == category else 0.0)

        matrix.append(features)
        labels.append(int(row[target_field]))

    return matrix, labels, feature_names


@dataclass
class LogisticRegressionGD:
    """Small pure-Python logistic regression for interview-sized datasets."""

    learning_rate: float = 0.1
    epochs: int = 400
    class_weight_positive: float = 1.0
    weights: List[float] | None = None
    bias: float = 0.0

    def fit(self, features: Sequence[Sequence[float]], labels: Sequence[int]) -> None:
        if not features:
            raise ValueError("features must not be empty")

        width = len(features[0])
        self.weights = [0.0] * width
        self.bias = 0.0

        for _ in range(self.epochs):
            gradient = [0.0] * width
            bias_gradient = 0.0

            for row, label in zip(features, labels):
                prediction = self._sigmoid(self._linear(row))
                error = prediction - label
                weight = self.class_weight_positive if label == 1 else 1.0

                for index, value in enumerate(row):
                    gradient[index] += error * value * weight
                bias_gradient += error * weight

            scale = 1.0 / len(features)
            for index in range(width):
                self.weights[index] -= self.learning_rate * gradient[index] * scale
            self.bias -= self.learning_rate * bias_gradient * scale

    def predict_proba(self, features: Sequence[Sequence[float]]) -> List[float]:
        return [self._sigmoid(self._linear(row)) for row in features]

    def predict(self, features: Sequence[Sequence[float]], threshold: float = 0.5) -> List[int]:
        return [1 if probability >= threshold else 0 for probability in self.predict_proba(features)]

    def _linear(self, row: Sequence[float]) -> float:
        if self.weights is None:
            raise ValueError("model has not been fit")
        return sum(weight * value for weight, value in zip(self.weights, row)) + self.bias

    @staticmethod
    def _sigmoid(value: float) -> float:
        clipped = max(min(value, 20), -20)
        return 1.0 / (1.0 + math.exp(-clipped))


def train_baseline_classifier(
    rows: Sequence[Row],
    target_field: str,
) -> Dict[str, Any]:
    """Train a small logistic-regression baseline with in-code preprocessing."""
    plan = build_preprocessing_plan(rows, target_field)
    matrix, labels, feature_names = preprocess_rows(rows, target_field, plan)

    split_index = max(1, int(len(rows) * 0.8))
    train_X, valid_X = matrix[:split_index], matrix[split_index:]
    train_y, valid_y = labels[:split_index], labels[split_index:]

    model = LogisticRegressionGD()
    model.fit(train_X, train_y)

    valid_probs = model.predict_proba(valid_X)
    valid_preds = [1 if probability >= 0.5 else 0 for probability in valid_probs]

    return {
        "model": model,
        "plan": plan,
        "feature_names": feature_names,
        "validation_predictions": valid_preds,
        "validation_probabilities": valid_probs,
        "validation_accuracy": accuracy_score(valid_y, valid_preds) if valid_y else 0.0,
    }


def train_class_imbalanced_classifier(
    rows: Sequence[Row],
    target_field: str,
) -> Dict[str, Any]:
    """Train logistic regression with a positive-class weight and PR-style metrics."""
    plan = build_preprocessing_plan(rows, target_field)
    matrix, labels, feature_names = preprocess_rows(rows, target_field, plan)

    split_index = max(1, int(len(rows) * 0.8))
    train_X, valid_X = matrix[:split_index], matrix[split_index:]
    train_y, valid_y = labels[:split_index], labels[split_index:]

    positives = max(1, sum(train_y))
    negatives = max(1, len(train_y) - positives)
    positive_weight = negatives / positives

    model = LogisticRegressionGD(class_weight_positive=positive_weight)
    model.fit(train_X, train_y)
    valid_probs = model.predict_proba(valid_X)
    valid_preds = [1 if probability >= 0.5 else 0 for probability in valid_probs]

    precision, recall = precision_recall(valid_y, valid_preds) if valid_y else (0.0, 0.0)
    return {
        "model": model,
        "plan": plan,
        "feature_names": feature_names,
        "positive_weight": positive_weight,
        "precision": precision,
        "recall": recall,
    }


def add_rolling_user_features(
    rows: Sequence[Row],
    user_field: str = "user_id",
    timestamp_field: str = "event_ts",
    value_field: str = "amount",
    window_days: int = 7,
) -> List[Row]:
    """Build point-in-time-safe rolling features by excluding the current row."""
    grouped: Dict[Any, List[Row]] = defaultdict(list)
    for row in rows:
        grouped[row[user_field]].append(dict(row))

    output: List[Row] = []
    for _, user_rows in sorted(grouped.items(), key=lambda item: item[0]):
        ordered = sorted(user_rows, key=lambda row: _parse_timestamp(row[timestamp_field]))
        history: List[tuple[datetime, float]] = []

        for row in ordered:
            event_ts = _parse_timestamp(row[timestamp_field])
            cutoff = event_ts - timedelta(days=window_days)
            history = [(ts, value) for ts, value in history if ts >= cutoff]

            row[f"rolling_{window_days}_count"] = len(history)
            row[f"rolling_{window_days}_sum"] = sum(value for _, value in history)

            history.append((event_ts, float(row[value_field])))
            output.append(row)

    return output


def permutation_feature_importance(
    model: LogisticRegressionGD,
    features: Sequence[Sequence[float]],
    labels: Sequence[int],
    feature_names: Sequence[str],
    seed: int = 42,
) -> List[Row]:
    """Measure accuracy drop after shuffling one feature at a time."""
    baseline_predictions = model.predict(features)
    baseline_accuracy = accuracy_score(labels, baseline_predictions)
    rng = random.Random(seed)
    importances: List[Row] = []

    for index, feature_name in enumerate(feature_names):
        shuffled = [list(row) for row in features]
        column = [row[index] for row in shuffled]
        rng.shuffle(column)

        for row_number, row in enumerate(shuffled):
            row[index] = column[row_number]

        shuffled_accuracy = accuracy_score(labels, model.predict(shuffled))
        importances.append(
            {
                "feature": feature_name,
                "importance": baseline_accuracy - shuffled_accuracy,
            }
        )

    return sorted(importances, key=lambda row: row["importance"], reverse=True)


def time_series_splits(
    rows: Sequence[Row],
    timestamp_field: str,
    n_splits: int,
) -> List[Dict[str, List[Row]]]:
    """Create expanding-window train/validation splits in chronological order."""
    ordered = sorted((dict(row) for row in rows), key=lambda row: _parse_timestamp(row[timestamp_field]))
    fold_size = max(1, len(ordered) // (n_splits + 1))
    splits: List[Dict[str, List[Row]]] = []

    for fold in range(1, n_splits + 1):
        train_end = fold * fold_size
        valid_end = min(len(ordered), train_end + fold_size)
        train_rows = ordered[:train_end]
        valid_rows = ordered[train_end:valid_end]
        if train_rows and valid_rows:
            splits.append({"train": train_rows, "validation": valid_rows})

    return splits


TOKEN_PATTERN = re.compile(r"[a-z0-9']+")


def _tokenize(text: str) -> List[str]:
    return TOKEN_PATTERN.findall(text.lower())


@dataclass
class NaiveBayesTextClassifier:
    alpha: float = 1.0
    class_token_counts: Dict[int, Counter[str]] | None = None
    class_counts: Counter[int] | None = None
    vocabulary: set[str] | None = None

    def fit(self, texts: Sequence[str], labels: Sequence[int]) -> None:
        self.class_token_counts = defaultdict(Counter)
        self.class_counts = Counter(labels)
        self.vocabulary = set()

        for text, label in zip(texts, labels):
            tokens = _tokenize(text)
            self.class_token_counts[label].update(tokens)
            self.vocabulary.update(tokens)

    def predict(self, texts: Sequence[str]) -> List[int]:
        if self.class_token_counts is None or self.class_counts is None or self.vocabulary is None:
            raise ValueError("model has not been fit")

        total_rows = sum(self.class_counts.values())
        vocabulary_size = max(1, len(self.vocabulary))
        predictions: List[int] = []

        for text in texts:
            tokens = _tokenize(text)
            best_label = None
            best_score = float("-inf")

            for label, count in self.class_counts.items():
                total_tokens = sum(self.class_token_counts[label].values())
                log_prob = math.log(count / total_rows)

                for token in tokens:
                    token_count = self.class_token_counts[label][token]
                    smoothed = (token_count + self.alpha) / (total_tokens + self.alpha * vocabulary_size)
                    log_prob += math.log(smoothed)

                if log_prob > best_score:
                    best_score = log_prob
                    best_label = label

            predictions.append(int(best_label))

        return predictions


def train_text_baseline(
    rows: Sequence[Row],
    text_field: str,
    target_field: str,
) -> Dict[str, Any]:
    """Train a small multinomial Naive Bayes baseline for text classification."""
    split_index = max(1, int(len(rows) * 0.8))
    train_rows = rows[:split_index]
    valid_rows = rows[split_index:]

    model = NaiveBayesTextClassifier()
    model.fit([row[text_field] for row in train_rows], [int(row[target_field]) for row in train_rows])

    valid_texts = [row[text_field] for row in valid_rows]
    valid_labels = [int(row[target_field]) for row in valid_rows]
    predictions = model.predict(valid_texts)

    return {
        "model": model,
        "validation_predictions": predictions,
        "validation_accuracy": accuracy_score(valid_labels, predictions) if valid_labels else 0.0,
    }


def accuracy_score(labels: Sequence[int], predictions: Sequence[int]) -> float:
    if not labels:
        return 0.0
    matches = sum(1 for label, prediction in zip(labels, predictions) if label == prediction)
    return matches / len(labels)


def precision_recall(labels: Sequence[int], predictions: Sequence[int]) -> tuple[float, float]:
    true_positive = sum(1 for label, prediction in zip(labels, predictions) if label == 1 and prediction == 1)
    false_positive = sum(1 for label, prediction in zip(labels, predictions) if label == 0 and prediction == 1)
    false_negative = sum(1 for label, prediction in zip(labels, predictions) if label == 1 and prediction == 0)

    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else 0.0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else 0.0
    return precision, recall
