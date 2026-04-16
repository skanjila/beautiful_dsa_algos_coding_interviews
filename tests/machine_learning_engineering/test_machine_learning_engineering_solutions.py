import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from machine_learning_engineering.solutions import (
    calibration_bins,
    chunk_document,
    citation_coverage,
    dcg_at_k,
    expected_calibration_error,
    keyword_retrieve,
    ndcg_at_k,
    population_stability_index,
    precision_at_k,
    recall_at_k,
    reciprocal_rank_fusion,
)


def test_precision_and_recall_at_k():
    relevance = [1, 0, 1, 1]
    assert precision_at_k(relevance, 2) == 0.5
    assert recall_at_k(relevance, 3, total_relevant=3) == 2 / 3


def test_dcg_and_ndcg():
    relevance = [1, 0, 1]
    assert dcg_at_k(relevance, 3) > 0
    assert 0.0 <= ndcg_at_k(relevance, 3) <= 1.0


def test_calibration_bins_and_ece():
    probabilities = [0.1, 0.2, 0.8, 0.9]
    labels = [0, 0, 1, 1]
    bins = calibration_bins(probabilities, labels, bins=2)
    assert bins
    assert 0.0 <= expected_calibration_error(probabilities, labels, bins=2) <= 1.0


def test_population_stability_index_for_changed_distribution():
    baseline = [0.1, 0.2, 0.2, 0.3, 0.4]
    current = [0.6, 0.7, 0.8, 0.8, 0.9]
    assert population_stability_index(baseline, current, bins=5) > 0


def test_chunk_document_creates_overlapping_chunks():
    text = "one two three four five six seven eight nine ten"
    chunks = chunk_document(text, chunk_size=4, overlap=1)
    assert len(chunks) >= 3
    assert chunks[0].startswith("one two")


def test_keyword_retrieve_scores_overlap():
    docs = {
        "a": "feed ranking ranking quality",
        "b": "fraud review queue",
        "c": "ranking retrieval latency",
    }
    results = keyword_retrieve("ranking latency", docs, top_k=2)
    assert len(results) == 2
    assert results[0].chunk_id in {"a", "c"}


def test_reciprocal_rank_fusion_combines_lists():
    fused = reciprocal_rank_fusion([["a", "b", "c"], ["b", "a", "d"]])
    assert fused[0][0] in {"a", "b"}
    assert len(fused) == 4


def test_citation_coverage_is_fractional():
    answer = "ranking latency quality"
    support = ["quality and latency are measured", "ranking systems need metrics"]
    score = citation_coverage(answer, support)
    assert 0.0 <= score <= 1.0
    assert score > 0
