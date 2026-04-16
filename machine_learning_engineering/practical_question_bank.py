from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class PracticalQuestion:
    slug: str
    category: str
    difficulty: str
    question: str
    interview_approach: str
    modeling_approach: str
    system_approach: str
    deep_dive: str


PRACTICAL_QUESTION_BANK: List[PracticalQuestion] = [
    PracticalQuestion(
        slug="design-feed-ranking",
        category="ranking",
        difficulty="hard",
        question="Design a feed ranking system for a social product.",
        interview_approach="Clarify the objective first: engagement, quality, retention, safety, or a mixture. Then split the design into candidate generation, lightweight ranking, heavy reranking, and feedback loops rather than jumping directly to one model.",
        modeling_approach="Use historical interaction signals, creator and content features, freshness, and embeddings. Discuss multi-objective ranking, label definitions such as click, dwell, reaction, or hide, and how exploration is needed to reduce feedback loops.",
        system_approach="Describe candidate sources, feature computation, online feature freshness, low-latency inference, caching, shadow launches, and monitoring for latency plus user-quality metrics. Call out offline-online skew and abuse or integrity constraints.",
        deep_dive="This is a canonical MAANG MLE question because it combines product thinking with ranking architecture. Strong answers separate retrieval from ranking, explain stage-specific metrics, mention exploration, and describe why the best offline ranker may not be the best production system under p99 and safety constraints.",
    ),
    PracticalQuestion(
        slug="design-recommendation-system",
        category="recommendation",
        difficulty="hard",
        question="Design a recommendation system for videos, products, or music.",
        interview_approach="Start by defining what recommendation quality means for this product: click, watch time, purchase, save rate, or long-term retention. Then walk through cold start, candidate generation, ranking, serving, and feedback loops in order.",
        modeling_approach="Cover collaborative filtering, content features, embeddings, retrieval models, rerankers, and hybrid systems. Mention user and item cold start separately, and explain how implicit feedback differs from explicit labels.",
        system_approach="Discuss batch versus online features, ANN or approximate retrieval, candidate freshness, heavy versus light models, experiment design, and abuse or safety filters that may run before or after ranking.",
        deep_dive="Interviewers use this to see whether you understand recommender systems as a product policy and infrastructure problem, not just a matrix factorization problem. The strongest answers mention exploration, popularity bias, long-term effects, and quality guardrails beyond raw CTR.",
    ),
    PracticalQuestion(
        slug="design-search-ranking",
        category="search",
        difficulty="hard",
        question="Design a search ranking or query-understanding system.",
        interview_approach="Clarify the search surface first: web search, internal search, enterprise documents, or app search. Then separate retrieval, query understanding, ranking, answer generation, and evaluation.",
        modeling_approach="Discuss lexical retrieval, semantic retrieval, query rewriting, spelling correction, embeddings, click models, relevance labels, and top-of-list metrics like NDCG or MRR. If appropriate, mention LLM-assisted query understanding or answer generation as a later stage rather than the entire system.",
        system_approach="Explain indexing, freshness, latency budgets, online feature access, reranking, logging, judgment datasets, and how offline relevance metrics map imperfectly to online outcomes. Mention fallback behavior when retrieval or generation fails.",
        deep_dive="This category is especially relevant for Apple, Google, and assistant-oriented roles. Strong answers show comfort with retrieval and ranking metrics, not only generic classification metrics. They also make clear that search quality requires data quality, evaluation design, and product judgment.",
    ),
    PracticalQuestion(
        slug="design-ads-ctr-prediction",
        category="ads",
        difficulty="hard",
        question="Design an ads CTR or conversion prediction system.",
        interview_approach="State the auction or ranking objective before describing the model. Clarify whether the system optimizes CTR, CVR, expected value, or a blended business objective with constraints.",
        modeling_approach="Talk about high-cardinality sparse features, embeddings, calibration, delayed conversion labels, multi-task learning, and counterfactual bias. Mention why calibration often matters more here than in a generic benchmark setting.",
        system_approach="Describe feature freshness, budget and pacing interactions, online inference constraints, delayed feedback handling, exploration, and guardrails against bad-user experience or advertiser gaming.",
        deep_dive="Ads questions are common because they force you to connect ML metrics to revenue and auction mechanics. Good candidates explain that prediction quality is only one part of the system and that serving, calibration, and delayed reward structure dominate many design choices.",
    ),
    PracticalQuestion(
        slug="design-abuse-detection",
        category="trust-safety",
        difficulty="medium",
        question="Design a spam, fraud, or abuse detection system.",
        interview_approach="Start with the cost of misses versus false alarms, then define whether the system blocks automatically, ranks risk, or feeds a human review queue. That decision changes the entire operating point.",
        modeling_approach="Explain rare-event modeling, thresholding, calibration, reviewer feedback, active learning, and adversarial adaptation. If the attacker changes behavior quickly, say so explicitly and mention short feedback loops.",
        system_approach="Cover streaming signals, latency, human-in-the-loop workflows, queue budgets, retraining cadence, slice monitoring, and safe rollback behavior. Include how you would log outcomes for future learning.",
        deep_dive="This question rewards operational realism. The best answers mention reviewer capacity, policy evolution, label delay, and the fact that the system is being attacked. Treating it like a static classifier is usually too shallow.",
    ),
    PracticalQuestion(
        slug="design-llm-rag",
        category="llm-genai",
        difficulty="hard",
        question="Design a retrieval-augmented generation assistant over a private document corpus.",
        interview_approach="Define the task, failure cost, freshness needs, and latency budget first. Then walk through ingestion, chunking, indexing, retrieval, reranking, prompt construction, answer generation, safety, and evaluation.",
        modeling_approach="Describe embedding strategy, retrieval quality, reranking, prompt templates, citation grounding, answer abstention, and task-specific evaluation. Mention that generation quality should not hide retrieval failures.",
        system_approach="Discuss document updates, index rebuilds, caching, cost control, prompt logging policy, privacy, fallback responses, offline evaluation sets, and online human-feedback or thumb signals.",
        deep_dive="This is increasingly relevant in applied-AI interviews, but strong answers still look like disciplined system design rather than prompt hacking. Interviewers want to hear separate reasoning about retrieval, generation, safety, latency, and cost.",
    ),
    PracticalQuestion(
        slug="design-feature-store-pipeline",
        category="ml-platform",
        difficulty="medium",
        question="Design a feature pipeline or feature store workflow for model training and serving.",
        interview_approach="Start by naming the actual problem: offline-online consistency, feature reuse, freshness, lineage, or point-in-time correctness. Then structure the answer around feature definition, computation, storage, serving, and validation.",
        modeling_approach="Explain that the feature store is model-adjacent rather than the model itself. Mention point-in-time joins, backfills, high-cardinality entities, feature freshness classes, and data validation before training or serving.",
        system_approach="Discuss batch features, streaming features, online key-value serving, offline backfills, schema evolution, lineage, and parity checks. Mention how training examples are built without leaking future events.",
        deep_dive="MLE interviews often use this to test whether the candidate understands production data semantics, not just training code. Strong answers distinguish between convenience and correctness and explain how the platform reduces repeated mistakes without magically fixing bad features.",
    ),
    PracticalQuestion(
        slug="design-model-monitoring",
        category="ml-ops",
        difficulty="medium",
        question="Design a production monitoring and alerting strategy for an ML model.",
        interview_approach="Break the problem into serving health, input health, output health, and delayed label quality. Saying those layers early makes the answer feel controlled instead of improvised.",
        modeling_approach="Talk about feature drift, score drift, calibration drift, threshold behavior, slice monitoring, delayed labels, and how to tell the difference between expected seasonality and genuine degradation.",
        system_approach="Include request latency, error rate, schema violations, feature freshness, score distribution dashboards, label joins when they arrive, alert thresholds, canary comparisons, and rollback criteria.",
        deep_dive="Many candidates answer this as 'track accuracy' and stop there, which is not enough. In production you need fast leading indicators before labels arrive. The strongest answers mention business KPIs, delayed supervision, and how monitoring ties into retraining or rollback decisions.",
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
        or normalized in entry.modeling_approach.lower()
        or normalized in entry.system_approach.lower()
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
    sections = ["# Machine Learning Engineering Practical Interview Problems", ""]
    for category in list_categories():
        sections.append(f"## {category.replace('-', ' ').title()}")
        sections.append("")
        for entry in filter_by_category(category):
            sections.append(f"### {entry.question}")
            sections.append(f"- Difficulty: `{entry.difficulty}`")
            sections.append(f"- Interview approach: {entry.interview_approach}")
            sections.append(f"- Modeling approach: {entry.modeling_approach}")
            sections.append(f"- System approach: {entry.system_approach}")
            sections.append(f"- Deep dive: {entry.deep_dive}")
            sections.append("")
    return "\n".join(sections)
