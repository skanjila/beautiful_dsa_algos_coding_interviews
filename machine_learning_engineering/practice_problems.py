from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class PracticeProblem:
    slug: str
    section: str
    difficulty: str
    function_name: str
    prompt: str
    status: str


PRACTICE_PROBLEMS: List[PracticeProblem] = [
    PracticeProblem(
        slug="compute-average-precision",
        section="evaluation",
        difficulty="medium",
        function_name="compute_average_precision",
        prompt="Implement average precision for a ranked list of binary relevance labels.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="compute-brier-score",
        section="evaluation",
        difficulty="easy",
        function_name="compute_brier_score",
        prompt="Implement Brier score for predicted probabilities and binary labels.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="detect-feature-freshness-gaps",
        section="ml-platform",
        difficulty="medium",
        function_name="detect_feature_freshness_gaps",
        prompt="Given feature timestamps and request timestamps, identify stale features that violate freshness SLAs.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="build-point-in-time-dataset-index",
        section="feature-engineering",
        difficulty="hard",
        function_name="build_point_in_time_dataset_index",
        prompt="Build a point-in-time-safe join index from events and label timestamps.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="compute-auc-from-pairs",
        section="modeling",
        difficulty="medium",
        function_name="compute_auc_from_pairs",
        prompt="Implement ROC AUC from prediction scores and binary labels without external ML libraries.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="rerank-by-business-rules",
        section="ranking",
        difficulty="medium",
        function_name="rerank_by_business_rules",
        prompt="Rerank candidate items by combining model scores with freshness and diversity constraints.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="sample-hard-negatives",
        section="retrieval-ranking",
        difficulty="hard",
        function_name="sample_hard_negatives",
        prompt="Given positives and retrieval scores, sample hard negatives for ranking training.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="simulate-bandit-exploration",
        section="product-ml",
        difficulty="hard",
        function_name="simulate_bandit_exploration",
        prompt="Implement a simple epsilon-greedy exploration simulator over item reward estimates.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="select-review-threshold",
        section="trust-safety",
        difficulty="medium",
        function_name="select_review_threshold",
        prompt="Choose a threshold that respects both precision targets and human review queue capacity.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="map-documents-to-chunks",
        section="llm-genai",
        difficulty="easy",
        function_name="map_documents_to_chunks",
        prompt="Chunk multiple documents into overlapping segments while preserving source document IDs.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="score-rag-answer-groundedness",
        section="llm-genai",
        difficulty="medium",
        function_name="score_rag_answer_groundedness",
        prompt="Score whether an answer is grounded in retrieved support snippets.",
        status="stubbed",
    ),
    PracticeProblem(
        slug="build-retrieval-eval-report",
        section="llm-genai",
        difficulty="medium",
        function_name="build_retrieval_eval_report",
        prompt="Aggregate retrieval hit rate, MRR, and citation coverage into a small evaluation report.",
        status="stubbed",
    ),
]


def list_sections() -> List[str]:
    return sorted({entry.section for entry in PRACTICE_PROBLEMS})


def list_stubbed_problem_slugs() -> List[str]:
    return [entry.slug for entry in PRACTICE_PROBLEMS if entry.status == "stubbed"]
