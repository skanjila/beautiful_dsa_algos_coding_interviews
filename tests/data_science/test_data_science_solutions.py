import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from data_science.solutions import (
    add_rolling_user_features,
    build_preprocessing_plan,
    infer_feature_types,
    permutation_feature_importance,
    preprocess_rows,
    time_series_splits,
    train_baseline_classifier,
    train_class_imbalanced_classifier,
    train_text_baseline,
)


TABULAR_ROWS = [
    {"age": 25, "income": 50_000, "city": "SF", "label": 0},
    {"age": 45, "income": 90_000, "city": "NY", "label": 1},
    {"age": 23, "income": 48_000, "city": "SF", "label": 0},
    {"age": 52, "income": 110_000, "city": "NY", "label": 1},
    {"age": 29, "income": 58_000, "city": "LA", "label": 0},
    {"age": 48, "income": 99_000, "city": "NY", "label": 1},
]


def test_infer_feature_types_splits_numeric_and_categorical():
    result = infer_feature_types(TABULAR_ROWS, target_field="label")
    assert result["numeric"] == ["age", "income"]
    assert result["categorical"] == ["city"]


def test_build_preprocessing_plan_and_matrix_have_expected_shape():
    plan = build_preprocessing_plan(TABULAR_ROWS, target_field="label")
    matrix, labels, feature_names = preprocess_rows(TABULAR_ROWS, "label", plan)

    assert len(matrix) == len(TABULAR_ROWS)
    assert labels == [row["label"] for row in TABULAR_ROWS]
    assert "age" in feature_names
    assert "income" in feature_names
    assert any(name.startswith("city=") for name in feature_names)


def test_train_baseline_classifier_returns_working_model_and_metrics():
    result = train_baseline_classifier(TABULAR_ROWS, target_field="label")

    assert 0.0 <= result["validation_accuracy"] <= 1.0
    assert result["feature_names"]
    assert result["model"].weights is not None


def test_train_class_imbalanced_classifier_returns_precision_and_recall():
    rows = TABULAR_ROWS + [{"age": 31, "income": 62_000, "city": "LA", "label": 0}] * 4

    result = train_class_imbalanced_classifier(rows, target_field="label")

    assert result["positive_weight"] >= 1.0
    assert 0.0 <= result["precision"] <= 1.0
    assert 0.0 <= result["recall"] <= 1.0


def test_add_rolling_user_features_excludes_current_row_from_history():
    rows = [
        {"user_id": "u1", "event_ts": "2025-01-01T00:00:00Z", "amount": 10},
        {"user_id": "u1", "event_ts": "2025-01-03T00:00:00Z", "amount": 15},
        {"user_id": "u1", "event_ts": "2025-01-05T00:00:00Z", "amount": 5},
    ]

    result = add_rolling_user_features(rows, window_days=7)

    assert result[0]["rolling_7_count"] == 0
    assert result[1]["rolling_7_count"] == 1
    assert result[2]["rolling_7_sum"] == 25.0


def test_permutation_feature_importance_returns_sorted_importances():
    trained = train_baseline_classifier(TABULAR_ROWS, target_field="label")
    plan = trained["plan"]
    matrix, labels, feature_names = preprocess_rows(TABULAR_ROWS, "label", plan)

    importances = permutation_feature_importance(
        trained["model"],
        matrix,
        labels,
        feature_names,
    )

    assert len(importances) == len(feature_names)
    assert importances[0]["importance"] >= importances[-1]["importance"]


def test_time_series_splits_preserve_chronological_order():
    rows = [
        {"event_ts": f"2025-01-0{day}T00:00:00Z", "label": day % 2}
        for day in range(1, 7)
    ]

    splits = time_series_splits(rows, timestamp_field="event_ts", n_splits=2)

    assert len(splits) == 2
    assert splits[0]["train"][0]["event_ts"] < splits[0]["validation"][0]["event_ts"]
    assert len(splits[1]["train"]) > len(splits[0]["train"])


def test_train_text_baseline_produces_predictions():
    rows = [
        {"text": "cheap sale discount", "label": 1},
        {"text": "exclusive premium quality", "label": 0},
        {"text": "discount coupon today", "label": 1},
        {"text": "premium craftsmanship", "label": 0},
        {"text": "flash sale limited", "label": 1},
        {"text": "luxury tailored design", "label": 0},
    ]

    result = train_text_baseline(rows, text_field="text", target_field="label")

    assert 0.0 <= result["validation_accuracy"] <= 1.0
    assert len(result["validation_predictions"]) == 2
