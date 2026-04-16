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
        slug="mle-loop-shape",
        category="interview-strategy",
        difficulty="easy",
        question="What does a typical MAANG-style machine learning engineer interview loop usually test?",
        short_answer="It typically tests coding and DSA, applied ML fundamentals, feature engineering and evaluation, ML system design, production and MLOps judgment, and communication under product constraints.",
        deep_dive="The key distinction is that MLE loops are not just data science plus coding. Interviewers usually want evidence that you can move across the full lifecycle: framing a prediction problem, choosing metrics, building leakage-safe data, training and evaluating a model, reasoning about latency and scale, launching safely, and monitoring drift or regressions in production.",
    ),
    QuestionAnswer(
        slug="coding-bar-for-mle",
        category="coding",
        difficulty="easy",
        question="How strong does DSA performance need to be for an MLE interview at top tech companies?",
        short_answer="Usually strong enough to clear a standard software-engineering-style coding screen, even if the role is applied rather than infrastructure-heavy.",
        deep_dive="Many candidates underprepare here. In top-company MLE loops, coding is often used as a baseline filter for implementation rigor, debugging ability, and problem decomposition under time pressure. The exact bar varies by team, but weak coding can block otherwise strong ML candidates, especially at companies where MLE is treated as a software engineering role with ML depth.",
    ),
    QuestionAnswer(
        slug="sql-for-mle",
        category="coding",
        difficulty="easy",
        question="Why is SQL still important for machine learning engineers?",
        short_answer="Because MLEs often need to define labels, build training sets, validate joins, compute features, and analyze experiment slices before any model training happens.",
        deep_dive="In practice, many modeling failures start as data-shaping failures. SQL is how you inspect cohorts, remove leakage, compute event windows, debug skew, and sanity-check offline metrics. Interviewers use SQL or data-manipulation questions to check whether you can reason about the data pipeline, not just the estimator.",
    ),
    QuestionAnswer(
        slug="offline-vs-online-metrics",
        category="evaluation",
        difficulty="medium",
        question="How do you think about offline metrics versus online metrics in an MLE interview?",
        short_answer="Offline metrics tell you whether the model appears to learn the task; online metrics tell you whether the deployed system improves the real product outcome.",
        deep_dive="A strong answer separates model-quality metrics like AUC, log loss, NDCG, recall, BLEU, or calibration from product metrics like CTR, session length, abuse rate, retention, or conversion. Interviewers want to hear that a model can improve offline while hurting product behavior because of feedback loops, latency, poor thresholding, or metric mismatch.",
    ),
    QuestionAnswer(
        slug="dataset-shift-triad",
        category="ml-ops",
        difficulty="medium",
        question="What is the difference between data drift, label drift, and concept drift?",
        short_answer="Data drift changes the input distribution, label drift changes target prevalence, and concept drift changes the relationship between features and labels.",
        deep_dive="This question tests whether you can monitor the right layer of the system. Input drift may require feature validation or retraining, label-prevalence drift changes calibration and threshold policy, and concept drift is the hardest because the mapping itself has changed. Good answers mention delayed labels, monitoring windows, and which signals are actually available online.",
    ),
    QuestionAnswer(
        slug="label-leakage",
        category="feature-engineering",
        difficulty="medium",
        question="What is the most common leakage mistake in production ML systems?",
        short_answer="Using features, joins, or aggregates that would not actually be available at prediction time.",
        deep_dive="Interviewers care about point-in-time correctness more than textbook definitions. Leakage often appears through future events in aggregates, post-outcome workflow states, backfilled dimensions, or fitting transformations on the full dataset before the split. Strong answers define a prediction timestamp and evaluate every feature against that boundary.",
    ),
    QuestionAnswer(
        slug="calibration-in-production",
        category="evaluation",
        difficulty="hard",
        question="Why does calibration matter in production ML systems?",
        short_answer="Because many downstream decisions depend on the probability value itself, not just the ranking of examples.",
        deep_dive="If a score is used for thresholding, human review queues, risk scoring, budget allocation, ranking blends, or product triggers, miscalibration can damage business decisions even when ranking metrics look strong. Good answers mention reliability curves, Brier score, Platt scaling, isotonic regression, and when calibration should be evaluated on temporally correct data.",
    ),
    QuestionAnswer(
        slug="class-imbalance-production",
        category="modeling",
        difficulty="medium",
        question="How do you handle a rare positive class in an MLE setting?",
        short_answer="Start with the business cost of false negatives versus false positives, then choose metrics, sampling, weighting, thresholding, and review workflows accordingly.",
        deep_dive="The most important part is not naming SMOTE or class weights first. In production, rare-event systems usually need threshold tuning, alert budgets, queue capacity thinking, calibration, and perhaps ranking rather than hard classification. Strong answers tie the modeling choice back to an operational decision like fraud review or abuse escalation.",
    ),
    QuestionAnswer(
        slug="feature-store-purpose",
        category="ml-platform",
        difficulty="medium",
        question="What problem does a feature store solve?",
        short_answer="It helps standardize feature definitions, reduce offline-online skew, improve reuse, and support consistent retrieval for training and serving.",
        deep_dive="A mature answer also mentions what a feature store does not solve automatically. It does not remove leakage by itself, and it does not guarantee good features. Interviewers want to hear about point-in-time joins, freshness, lineage, backfills, and whether online serving features are actually aligned with training semantics.",
    ),
    QuestionAnswer(
        slug="offline-online-skew",
        category="ml-platform",
        difficulty="medium",
        question="What causes offline-online skew and how would you reduce it?",
        short_answer="It is caused when the data or transformations used in training differ from what the model sees at inference time.",
        deep_dive="This can happen because of different code paths, delayed or missing features, null-handling mismatches, inconsistent normalization, or data source differences. Strong answers mention shared transformation code, canary validation, feature logging, training-serving parity tests, and monitoring distributions after deployment.",
    ),
    QuestionAnswer(
        slug="recommendation-funnel",
        category="ml-system-design",
        difficulty="medium",
        question="Why do recommendation and ranking systems often use multi-stage funnels?",
        short_answer="Because scoring every item with the most expensive model is too slow and too expensive, so systems retrieve broadly and rank more carefully on smaller candidate sets.",
        deep_dive="A strong MLE answer mentions retrieval, filtering, lightweight ranking, and heavyweight reranking. It should also include latency budgets, feature availability per stage, and different objectives per layer, such as recall in retrieval and precision or business value in reranking.",
    ),
    QuestionAnswer(
        slug="ranking-metrics",
        category="retrieval-ranking",
        difficulty="medium",
        question="What metrics matter for ranking or retrieval systems?",
        short_answer="Common offline metrics include precision@k, recall@k, MAP, MRR, and NDCG, while online metrics depend on the product goal such as CTR, dwell time, save rate, or long-term retention.",
        deep_dive="The main interview signal is whether you know that top-of-list quality matters more than overall classification accuracy. For search, recommendations, ads, and feed ranking, relevance must be evaluated at position-sensitive cutoffs. Strong answers also mention counterfactual bias, delayed rewards, and exploration-exploitation tradeoffs.",
    ),
    QuestionAnswer(
        slug="negative-sampling",
        category="retrieval-ranking",
        difficulty="hard",
        question="Why does negative sampling matter in retrieval and ranking pipelines?",
        short_answer="Because the training objective and data distribution depend heavily on which non-clicked or non-converted examples you treat as negatives.",
        deep_dive="Random negatives may be too easy and produce weak discrimination, while hard negatives better reflect ranking difficulty but can introduce bias if chosen poorly. Interviewers often use this question to test whether you understand that data generation is part of the model design, especially for search, recommendation, and candidate retrieval systems.",
    ),
    QuestionAnswer(
        slug="exploration-exploitation",
        category="product-ml",
        difficulty="hard",
        question="Why is exploration important in recommendation or ranking systems?",
        short_answer="Because if you only optimize based on previously exposed items, you create feedback loops and stop learning about potentially better content.",
        deep_dive="Pure exploitation traps the system inside its historical policy. Strong answers mention logging bias, popularity bias, bandit or exploration strategies, cold-start issues, and the difference between evaluation data collected under one policy versus another. This is one of the clearest signals that a candidate understands product ML instead of only static supervised learning.",
    ),
    QuestionAnswer(
        slug="cold-start",
        category="product-ml",
        difficulty="medium",
        question="How do you handle cold start for new users or new items?",
        short_answer="Use side information, popularity priors, exploration, embeddings from metadata, or hybrid retrieval strategies until enough interaction data arrives.",
        deep_dive="Interviewers usually want to hear separate answers for user cold start and item cold start. Good candidates mention contextual features, taxonomy, content-based retrieval, popularity backoffs, and guardrails that keep the system useful while learning. A strong answer also names the tradeoff between personalization quality and exploration cost.",
    ),
    QuestionAnswer(
        slug="model-debugging",
        category="modeling",
        difficulty="medium",
        question="How do you debug a model that looks good offline but performs poorly in production?",
        short_answer="Work through the pipeline systematically: training data quality, leakage, skew, thresholding, calibration, latency, missing features, and policy or user-feedback changes.",
        deep_dive="Interviewers value a structured debugging playbook more than one clever diagnosis. Strong answers break the problem into data, features, model, serving, and business-decision layers. The best candidates distinguish between model failure and system failure, for example a good model harmed by stale features or a poor threshold.",
    ),
    QuestionAnswer(
        slug="ab-testing-ml",
        category="experimentation",
        difficulty="medium",
        question="What is different about A/B testing an ML system compared with testing a normal product feature?",
        short_answer="ML systems create distribution shifts, delayed effects, policy feedback loops, and metric interpretation issues that make experimentation more subtle.",
        deep_dive="A strong answer mentions exposure logging, sample-ratio mismatch checks, delayed labels, interference between users, novelty effects, and the gap between optimizing a model score versus a business KPI. For ranking or recommendation systems, the experiment is often testing the whole decision policy, not just a model artifact.",
    ),
    QuestionAnswer(
        slug="latency-vs-quality",
        category="ml-system-design",
        difficulty="medium",
        question="How do you reason about latency versus model quality in an MLE interview?",
        short_answer="Treat latency as a first-class product constraint and design the model stack, feature access pattern, and serving architecture around a concrete budget.",
        deep_dive="Many answers stay too model-centric. Interviewers want to hear stage-specific budgets, cached features, approximate retrieval, batching, distillation, fallback behavior, and how p99 latency differs from average latency. The best candidates also mention that a slightly weaker model can win if it enables a much better user experience or system reliability.",
    ),
    QuestionAnswer(
        slug="batch-vs-online-inference",
        category="ml-platform",
        difficulty="medium",
        question="When would you choose batch inference versus online inference?",
        short_answer="Batch inference works when predictions can be precomputed cheaply enough and do not need fresh context; online inference is needed when decisions depend on current user state or real-time features.",
        deep_dive="This question tests systems judgment. Strong answers mention freshness, request latency, feature availability, cost, update cadence, and fallback modes. Many real systems use a hybrid approach, such as batch candidate generation with online reranking.",
    ),
    QuestionAnswer(
        slug="retraining-policy",
        category="ml-ops",
        difficulty="medium",
        question="How do you decide when to retrain a model?",
        short_answer="Based on a combination of business cadence, data freshness, observed drift, delayed-label feedback, and the operational cost of retraining.",
        deep_dive="A strong answer avoids saying 'retrain every day' without justification. Interviewers want to hear scheduled retraining plus performance-triggered retraining, validation gates, rollback plans, and awareness that more frequent retraining can increase instability if labels are noisy or delayed.",
    ),
    QuestionAnswer(
        slug="human-in-the-loop",
        category="reliability-safety",
        difficulty="medium",
        question="When should a production ML system include a human-in-the-loop review step?",
        short_answer="When errors are high cost, labels are ambiguous, safety matters, or review feedback can meaningfully improve system quality.",
        deep_dive="Good candidates mention fraud review, abuse moderation, medical screening, compliance workflows, and edge-case escalation. The strongest answers also connect thresholding to queue capacity, reviewer quality, label latency, and active-learning value.",
    ),
    QuestionAnswer(
        slug="fairness-and-slices",
        category="reliability-safety",
        difficulty="hard",
        question="How should fairness or subgroup performance be discussed in an MLE interview?",
        short_answer="By defining the impacted decision, identifying important slices, measuring performance across them, and explaining which fairness tradeoffs matter for the product.",
        deep_dive="Interviewers usually do not want a generic lecture. They want concrete operational thinking: which user groups or content classes matter, how label quality differs by slice, what tradeoffs exist between global and per-slice optimization, and how fairness monitoring fits into launch and retraining policy.",
    ),
    QuestionAnswer(
        slug="llm-evaluation",
        category="llm-genai",
        difficulty="hard",
        question="How is evaluating an LLM-powered system different from evaluating a standard classifier?",
        short_answer="The outputs are open-ended, probabilistic, and often require task-specific rubric evaluation, human review, retrieval checks, safety checks, and cost-latency tradeoff analysis.",
        deep_dive="A strong answer mentions that exact-match accuracy is often too weak. You may need rubric-based human evaluation, groundedness checks, tool-use success, hallucination rate, latency, cost per request, and user satisfaction. For retrieval-augmented generation, evaluate retrieval and generation separately as well as the end-to-end system.",
    ),
    QuestionAnswer(
        slug="rag-interview-shape",
        category="llm-genai",
        difficulty="medium",
        question="What should you cover when asked to design a retrieval-augmented generation system?",
        short_answer="Clarify the use case, define quality and latency targets, design ingestion and chunking, retrieval, ranking, prompt construction, caching, safety, evaluation, and feedback loops.",
        deep_dive="Recent MLE and applied-AI interviews increasingly use RAG as a systems question. Strong answers separate document freshness, embedding/index strategy, retrieval quality, reranking, answer generation, guardrails, and evaluation. The main signal is disciplined systems thinking, not naming the most recent model family.",
    ),
    QuestionAnswer(
        slug="apple-on-device-privacy",
        category="company-variants",
        difficulty="medium",
        question="What additional themes can show up in Apple-style MLE interviews?",
        short_answer="On-device inference, privacy-preserving design, search quality, low-latency serving, and tight hardware-software integration often matter more than in a generic big-tech prep plan.",
        deep_dive="This is worth calling out explicitly because not all MAANG-adjacent companies emphasize the same tradeoffs. Apple roles often highlight search, query understanding, answer quality, privacy, and systems that run across device and backend boundaries. That means candidates should be comfortable discussing evaluation data, inference optimization, and the product implications of privacy constraints.",
    ),
    QuestionAnswer(
        slug="communication-bar",
        category="interview-strategy",
        difficulty="easy",
        question="What communication pattern works best in a machine learning interview?",
        short_answer="Start with clarifying questions, define the objective and constraints, state the pattern you are using, and separate modeling choices from system and product choices.",
        deep_dive="A calm, structured answer often outperforms a technically denser but scattered one. In MLE interviews especially, you need to show that you can move between product goals, data assumptions, model choices, and production constraints without losing the thread. Interviewers reward candidates who narrate decisions cleanly and revisit tradeoffs explicitly.",
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
        or normalized in entry.slug.lower()
        or normalized in entry.category.lower()
    ]


def get_question_by_slug(slug: str) -> Optional[QuestionAnswer]:
    normalized = slug.strip().lower()
    for entry in QUESTION_BANK:
        if entry.slug == normalized:
            return entry
    return None


def render_markdown_study_guide() -> str:
    sections = ["# Machine Learning Engineering Question Bank", ""]
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
