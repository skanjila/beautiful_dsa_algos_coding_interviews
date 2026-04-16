from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple


def precision_at_k(relevance: Sequence[int], k: int) -> float:
    """Compute precision at k for a ranked list of binary relevance labels."""
    if k <= 0:
        raise ValueError("k must be positive")
    window = list(relevance[:k])
    if not window:
        return 0.0
    return sum(window) / len(window)


def recall_at_k(relevance: Sequence[int], k: int, total_relevant: int) -> float:
    """Compute recall at k given the total number of relevant items."""
    if total_relevant <= 0:
        return 0.0
    return sum(relevance[:k]) / total_relevant


def dcg_at_k(relevance: Sequence[int], k: int) -> float:
    """Discounted cumulative gain for graded or binary relevance."""
    score = 0.0
    for index, rel in enumerate(relevance[:k], start=1):
        score += rel / math.log2(index + 1)
    return score


def ndcg_at_k(relevance: Sequence[int], k: int) -> float:
    """Normalized DCG compares the current ranking with the ideal ranking."""
    actual = dcg_at_k(relevance, k)
    ideal = dcg_at_k(sorted(relevance, reverse=True), k)
    if ideal == 0:
        return 0.0
    return actual / ideal


def calibration_bins(
    probabilities: Sequence[float],
    labels: Sequence[int],
    bins: int = 10,
) -> List[Dict[str, float]]:
    """Bucket predictions to compare confidence with empirical accuracy."""
    if len(probabilities) != len(labels):
        raise ValueError("probabilities and labels must have the same length")
    if bins <= 0:
        raise ValueError("bins must be positive")

    bucket_counts = [0] * bins
    bucket_probability_sum = [0.0] * bins
    bucket_positive_sum = [0.0] * bins

    for probability, label in zip(probabilities, labels):
        bucket_index = min(int(probability * bins), bins - 1)
        bucket_counts[bucket_index] += 1
        bucket_probability_sum[bucket_index] += probability
        bucket_positive_sum[bucket_index] += label

    results: List[Dict[str, float]] = []
    for index in range(bins):
        if bucket_counts[index] == 0:
            continue
        results.append(
            {
                "bin_start": index / bins,
                "bin_end": (index + 1) / bins,
                "count": float(bucket_counts[index]),
                "avg_prediction": bucket_probability_sum[index] / bucket_counts[index],
                "empirical_rate": bucket_positive_sum[index] / bucket_counts[index],
            }
        )
    return results


def expected_calibration_error(
    probabilities: Sequence[float],
    labels: Sequence[int],
    bins: int = 10,
) -> float:
    """Weighted calibration gap across confidence buckets."""
    bucket_stats = calibration_bins(probabilities, labels, bins=bins)
    total = len(probabilities)
    if total == 0:
        return 0.0

    error = 0.0
    for bucket in bucket_stats:
        weight = bucket["count"] / total
        error += weight * abs(bucket["avg_prediction"] - bucket["empirical_rate"])
    return error


def population_stability_index(
    baseline: Sequence[float],
    current: Sequence[float],
    bins: int = 10,
) -> float:
    """Simple PSI implementation for drift-style distribution comparison."""
    if not baseline or not current:
        return 0.0
    if bins <= 0:
        raise ValueError("bins must be positive")

    minimum = min(min(baseline), min(current))
    maximum = max(max(baseline), max(current))
    if minimum == maximum:
        return 0.0

    width = (maximum - minimum) / bins
    edges = [minimum + width * step for step in range(bins + 1)]
    edges[-1] = maximum

    def bucketize(values: Sequence[float]) -> List[float]:
        counts = [0] * bins
        for value in values:
            index = bins - 1
            for bucket_index in range(bins):
                upper = edges[bucket_index + 1]
                if value <= upper or bucket_index == bins - 1:
                    index = bucket_index
                    break
            counts[index] += 1
        total = len(values)
        return [max(count / total, 1e-6) for count in counts]

    baseline_dist = bucketize(baseline)
    current_dist = bucketize(current)

    psi = 0.0
    for expected, observed in zip(baseline_dist, current_dist):
        psi += (observed - expected) * math.log(observed / expected)
    return psi


TOKEN_PATTERN = re.compile(r"[a-z0-9']+")


def simple_tokenize(text: str) -> List[str]:
    return TOKEN_PATTERN.findall(text.lower())


def chunk_document(text: str, chunk_size: int = 80, overlap: int = 20) -> List[str]:
    """Split a document into overlapping token chunks for simple RAG practice."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    tokens = simple_tokenize(text)
    if not tokens:
        return []

    chunks: List[str] = []
    start = 0
    step = chunk_size - overlap
    while start < len(tokens):
        chunk_tokens = tokens[start : start + chunk_size]
        if not chunk_tokens:
            break
        chunks.append(" ".join(chunk_tokens))
        start += step
    return chunks


@dataclass(frozen=True)
class RetrievedChunk:
    chunk_id: str
    text: str
    score: float


def keyword_retrieve(
    query: str,
    documents: Dict[str, str],
    top_k: int = 3,
) -> List[RetrievedChunk]:
    """Score chunks by token overlap for a lightweight retrieval baseline."""
    query_terms = Counter(simple_tokenize(query))
    scored: List[RetrievedChunk] = []

    for chunk_id, text in documents.items():
        doc_terms = Counter(simple_tokenize(text))
        overlap = sum(min(doc_terms[token], count) for token, count in query_terms.items())
        if overlap > 0:
            scored.append(RetrievedChunk(chunk_id=chunk_id, text=text, score=float(overlap)))

    return sorted(scored, key=lambda item: (-item.score, item.chunk_id))[:top_k]


def reciprocal_rank_fusion(rankings: Sequence[Sequence[str]], k: int = 60) -> List[Tuple[str, float]]:
    """Fuse multiple ranked lists using reciprocal rank fusion."""
    scores: Dict[str, float] = {}
    for ranking in rankings:
        for rank, item in enumerate(ranking, start=1):
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))


def citation_coverage(answer: str, supporting_chunks: Iterable[str]) -> float:
    """Approximate groundedness by measuring how much answer vocabulary is supported."""
    answer_terms = set(simple_tokenize(answer))
    if not answer_terms:
        return 0.0

    support_terms = set()
    for chunk in supporting_chunks:
        support_terms.update(simple_tokenize(chunk))

    supported = len(answer_terms & support_terms)
    return supported / len(answer_terms)
