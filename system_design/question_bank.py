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
        slug="functional-vs-non-functional-requirements",
        category="fundamentals",
        difficulty="easy",
        question="What is the difference between functional and non-functional requirements?",
        short_answer="Functional requirements describe what the system must do. Non-functional requirements describe qualities like latency, availability, durability, throughput, and security.",
        deep_dive="Start every system design interview by separating capabilities from constraints. Functional requirements define features such as 'users can upload photos' or 'clients can place orders'. Non-functional requirements define expectations such as 'p99 latency under 300ms', '99.95% availability', or 'must survive regional failure'. This split prevents vague designs because you can map each architectural choice back to a measurable constraint.",
    ),
    QuestionAnswer(
        slug="scale-estimation",
        category="fundamentals",
        difficulty="easy",
        question="Why do rough scale estimations matter in system design?",
        short_answer="Because they determine whether you need simple single-node components or distributed systems with sharding, caching, queues, and storage specialization.",
        deep_dive="Back-of-the-envelope math turns abstract requirements into engineering choices. Estimating reads per second, writes per second, storage growth, and bandwidth lets you decide whether a relational database is enough or whether you need partitioning, asynchronous pipelines, or object storage. Even rough estimates are better than hand-waving because they expose the dominant bottlenecks early.",
    ),
    QuestionAnswer(
        slug="latency-vs-throughput",
        category="fundamentals",
        difficulty="easy",
        question="How are latency and throughput different, and why do both matter?",
        short_answer="Latency is how long one request takes. Throughput is how many requests the system can handle over time. A good design balances both under realistic load.",
        deep_dive="A system can have low latency at low load and still collapse under bursty traffic because throughput limits were ignored. Likewise, a system can push high throughput through batching but increase user-visible latency. Interviews reward designs that call out which paths are latency-sensitive, such as login or checkout, and which paths are throughput-oriented, such as analytics ingestion or batch indexing.",
    ),
    QuestionAnswer(
        slug="capacity-planning",
        category="fundamentals",
        difficulty="medium",
        question="What is capacity planning in service design?",
        short_answer="Capacity planning is forecasting future demand and provisioning compute, storage, network, and dependency headroom before failures or saturation happen.",
        deep_dive="Capacity planning is not just 'how many servers do we need today'. It includes seasonal traffic, burst factors, storage retention, replication cost, and operational safety margin. Good designs note peak-to-average ratios, failover headroom, and the cost of one-zone or one-node failure. That is how you avoid designs that work only at the median case.",
    ),
    QuestionAnswer(
        slug="load-balancer-role",
        category="scaling",
        difficulty="easy",
        question="What problem does a load balancer solve?",
        short_answer="It distributes traffic across service instances, hides backend topology, and can terminate TLS, perform health checks, and support rolling deployments.",
        deep_dive="A load balancer decouples clients from individual service nodes. That enables horizontal scaling, blue-green or canary rollout patterns, and automatic removal of unhealthy instances. In interviews you should also mention that load balancers can become critical infrastructure themselves, so redundancy and health-check correctness matter.",
    ),
    QuestionAnswer(
        slug="horizontal-vs-vertical-scaling",
        category="scaling",
        difficulty="easy",
        question="What is the difference between horizontal and vertical scaling?",
        short_answer="Vertical scaling adds more resources to one machine. Horizontal scaling adds more machines. Horizontal scaling is usually more resilient but harder operationally.",
        deep_dive="Vertical scaling is simple until you hit machine or vendor limits. Horizontal scaling supports fault isolation and elasticity, but now you must think about stateless services, distributed caches, partitioning, and coordination costs. Strong answers explicitly state which components are easy to scale horizontally and which remain stateful choke points.",
    ),
    QuestionAnswer(
        slug="stateless-services",
        category="scaling",
        difficulty="medium",
        question="Why are stateless application services easier to scale?",
        short_answer="Because any instance can handle any request when state is moved to durable or shared stores such as databases, caches, or object storage.",
        deep_dive="Statelessness simplifies autoscaling, load balancing, restarts, and deploys. Sessions, in-memory workflow state, or sticky routing introduce coupling that makes outages and scaling harder. When a design needs stateful behavior, the answer should explain where that state lives, how it is replicated, and how failover works.",
    ),
    QuestionAnswer(
        slug="rate-limiting",
        category="scaling",
        difficulty="medium",
        question="Why is rate limiting important?",
        short_answer="It protects systems from abuse, noisy neighbors, accidental floods, and downstream overload while giving fairness and predictable degradation.",
        deep_dive="Rate limiting is a control-plane safeguard as much as a security feature. It caps bad clients, preserves headroom for good clients, and prevents retry storms from turning a partial outage into a full outage. Mention common algorithms such as token bucket, leaky bucket, and fixed or sliding windows, plus where the limiter runs: edge, API gateway, or service-local.",
    ),
    QuestionAnswer(
        slug="database-indexing",
        category="data",
        difficulty="easy",
        question="Why do indexes help databases, and what is the tradeoff?",
        short_answer="Indexes speed up reads for specific access patterns but increase write cost, storage usage, and maintenance complexity.",
        deep_dive="Indexes are only valuable when tied to real query paths. Over-indexing slows inserts and updates and bloats memory usage. Good system design answers connect indexes to access patterns such as 'lookup by user_id and created_at' rather than saying 'we will add indexes' generically.",
    ),
    QuestionAnswer(
        slug="sql-vs-nosql",
        category="data",
        difficulty="medium",
        question="When would you choose SQL over NoSQL, or the reverse?",
        short_answer="Use SQL when integrity, joins, and transactional consistency dominate. Use NoSQL when access patterns, scale shape, or flexible data models make distribution and denormalization more important.",
        deep_dive="This is not a religion question. Relational databases are often the right default for transactional systems because they give strong correctness guarantees and mature tooling. NoSQL systems can shine for wide-column access, key-value lookup, time-series workloads, or large-scale document retrieval. The right answer should tie the choice to access patterns, consistency needs, and operational tradeoffs.",
    ),
    QuestionAnswer(
        slug="sharding",
        category="data",
        difficulty="medium",
        question="What is sharding and what problems does it introduce?",
        short_answer="Sharding splits data across partitions so no single node stores or serves everything. It improves scale but complicates routing, rebalancing, joins, and hot-key handling.",
        deep_dive="Sharding is usually introduced when one database instance becomes the throughput or storage bottleneck. The difficult part is not the first partitioning cut; it is handling skew, repartitioning, tenant movement, and cross-shard operations. Good answers mention shard keys, hot partitions, and the need to align keys with access patterns.",
    ),
    QuestionAnswer(
        slug="replication",
        category="data",
        difficulty="medium",
        question="Why do systems replicate data?",
        short_answer="To improve availability, durability, and sometimes read throughput by keeping multiple copies of the same data.",
        deep_dive="Replication is fundamental for fault tolerance, but it creates tradeoffs around consistency and failover semantics. Synchronous replication improves correctness but can hurt write latency. Asynchronous replication improves latency and availability but creates replica lag and possible data loss windows. Strong answers describe which tradeoff the product can tolerate.",
    ),
    QuestionAnswer(
        slug="consistency-models",
        category="data",
        difficulty="hard",
        question="What does eventual consistency mean in practical terms?",
        short_answer="It means replicas may temporarily disagree after a write, but they converge if no new updates arrive.",
        deep_dive="Eventual consistency is acceptable when stale reads are tolerable for short periods, such as timelines, counters, or recommendations. It is dangerous for money movement, inventory reservation, or security decisions unless carefully bounded. Practical answers mention user-visible symptoms like delayed propagation, read-after-write inconsistencies, and how product requirements constrain acceptable staleness.",
    ),
    QuestionAnswer(
        slug="cache-why",
        category="caching",
        difficulty="easy",
        question="Why do systems add caches?",
        short_answer="Caches reduce latency and offload expensive backing stores by serving repeated reads from faster memory.",
        deep_dive="Caching works best for read-heavy, skewed-access workloads. But it also introduces consistency, invalidation, and cold-start issues. In interviews, say what is being cached, how it is keyed, what the TTL is, and what happens on a miss or stale entry.",
    ),
    QuestionAnswer(
        slug="cache-invalidation",
        category="caching",
        difficulty="medium",
        question="Why is cache invalidation considered hard?",
        short_answer="Because cached data can become stale, and keeping it fresh without destroying the performance benefit requires careful ownership and update strategy.",
        deep_dive="The hard part is not storing bytes in Redis; it is deciding when those bytes are wrong. Common strategies include TTLs, write-through, write-behind, cache-aside, and event-driven invalidation. You should mention the consistency implications of each. If correctness is critical, designs often reduce cache scope or avoid caching mutable hot paths entirely.",
    ),
    QuestionAnswer(
        slug="cache-aside",
        category="caching",
        difficulty="medium",
        question="What is the cache-aside pattern?",
        short_answer="The application reads from cache first, falls back to the database on a miss, then populates the cache for future requests.",
        deep_dive="Cache-aside is common because it is simple and keeps the cache optional. The tradeoffs are stale reads, thundering herds on popular misses, and duplicated read logic in the application. A complete answer notes mitigations such as request coalescing, jittered TTLs, and negative caching for not-found lookups.",
    ),
    QuestionAnswer(
        slug="cdn-role",
        category="caching",
        difficulty="easy",
        question="What role does a CDN play in system design?",
        short_answer="A CDN moves static or cacheable content closer to users, reducing origin load and lowering latency across regions.",
        deep_dive="CDNs are especially effective for images, videos, downloads, and public API responses with well-defined cache headers. They reduce egress from origin and improve global performance. Good answers mention cache key design, invalidation strategy, and that dynamic authenticated traffic usually needs more careful handling.",
    ),
    QuestionAnswer(
        slug="message-queues",
        category="messaging",
        difficulty="easy",
        question="When do you introduce a message queue?",
        short_answer="When work can be decoupled from the request path or when producers and consumers need buffering, smoothing, and failure isolation.",
        deep_dive="Queues are useful when the user does not need immediate completion, such as email delivery, image processing, or analytics pipelines. They help absorb bursts and isolate slow consumers, but they add delivery semantics, retries, dead-letter handling, and duplicate processing concerns. Mention idempotency whenever queues appear.",
    ),
    QuestionAnswer(
        slug="pub-sub-vs-queue",
        category="messaging",
        difficulty="medium",
        question="How is pub-sub different from a work queue?",
        short_answer="A work queue usually hands one message to one consumer group member. Pub-sub fans the same event out to multiple independent subscribers.",
        deep_dive="Use work queues when one worker should perform one job. Use pub-sub when multiple systems need the same event for different purposes, such as billing, analytics, notifications, and auditing. Many real systems use both patterns in different layers, so the answer should focus on delivery semantics and ownership.",
    ),
    QuestionAnswer(
        slug="idempotency",
        category="reliability",
        difficulty="medium",
        question="Why is idempotency important in distributed systems?",
        short_answer="Because retries are unavoidable, and idempotent operations prevent duplicates from causing double charges, duplicate emails, or corrupted state.",
        deep_dive="Distributed systems fail in partial ways, so clients and services retry. Without idempotency, 'at least once' delivery becomes business corruption. Good answers mention idempotency keys, deduplication tables, natural unique constraints, and operation semantics designed so repeated execution is safe.",
    ),
    QuestionAnswer(
        slug="timeouts-retries",
        category="reliability",
        difficulty="medium",
        question="Why must timeouts and retries be designed together?",
        short_answer="Because retries without timeouts hang indefinitely, and retries without limits or jitter can amplify outages into retry storms.",
        deep_dive="Timeouts bound how long a dependency can hold resources. Retries recover from transient errors. But naive retries increase load on an already degraded dependency. Strong answers mention retry budgets, exponential backoff, jitter, and which errors are safe to retry.",
    ),
    QuestionAnswer(
        slug="circuit-breaker",
        category="reliability",
        difficulty="medium",
        question="What is a circuit breaker and what problem does it solve?",
        short_answer="A circuit breaker stops repeated calls to a failing dependency so the system can fail fast instead of wasting resources on likely failures.",
        deep_dive="When a downstream service is unhealthy, repeated requests tie up threads, connections, and queue slots. A circuit breaker opens after a threshold of failures, then allows only limited probes until the dependency recovers. Mention that breakers reduce blast radius but must be tuned carefully to avoid masking partial recovery.",
    ),
    QuestionAnswer(
        slug="graceful-degradation",
        category="reliability",
        difficulty="hard",
        question="What does graceful degradation mean in system design?",
        short_answer="It means the system sheds non-critical work or serves reduced functionality instead of failing completely when under stress or dependency failure.",
        deep_dive="Examples include serving cached recommendations when the personalization service fails, disabling expensive search filters under extreme load, or showing stale timelines instead of errors. Graceful degradation is a product decision as much as a technical one because it requires deciding what is core and what is optional.",
    ),
    QuestionAnswer(
        slug="observability-pillars",
        category="observability",
        difficulty="easy",
        question="What are the core pillars of observability?",
        short_answer="Logs, metrics, and traces. Together they help explain what happened, how often it happened, and where the latency or failure occurred.",
        deep_dive="Metrics show aggregate health, logs provide detailed local context, and traces follow a request across service boundaries. In strong system design answers, observability is attached to critical flows, SLIs, and operational decisions, not added as a vague afterthought.",
    ),
    QuestionAnswer(
        slug="sli-slo-sla",
        category="observability",
        difficulty="medium",
        question="What is the difference between an SLI, SLO, and SLA?",
        short_answer="An SLI is a measured indicator, an SLO is the internal target for that indicator, and an SLA is the external agreement tied to consequences.",
        deep_dive="For example, an SLI might be successful request ratio, an SLO could be 99.9% monthly success, and an SLA could promise credits if availability drops below 99.5%. Mentioning these terms correctly signals operational maturity, especially when discussing alerting and product tradeoffs.",
    ),
    QuestionAnswer(
        slug="security-basics",
        category="security",
        difficulty="easy",
        question="What are the basic security concerns to cover in a service design?",
        short_answer="Authentication, authorization, secret management, transport encryption, input validation, auditability, and abuse protection.",
        deep_dive="Security should not be reduced to 'use HTTPS'. You need to know who the caller is, what they are allowed to do, how secrets are rotated, how PII is protected, and how suspicious activity is logged. Strong answers also mention least privilege and data minimization.",
    ),
    QuestionAnswer(
        slug="authentication-vs-authorization",
        category="security",
        difficulty="easy",
        question="What is the difference between authentication and authorization?",
        short_answer="Authentication verifies identity. Authorization determines what that identity is allowed to access or modify.",
        deep_dive="This matters because systems often implement login correctly but fail to enforce ownership or role checks in downstream services. In interviews, say where identity is established, how it propagates, and where access decisions are enforced.",
    ),
    QuestionAnswer(
        slug="multi-region",
        category="availability",
        difficulty="hard",
        question="Why do teams deploy services across multiple regions?",
        short_answer="To reduce latency for global users and improve survivability against regional outages.",
        deep_dive="Multi-region is expensive and hard. It complicates replication, failover, consistency, traffic steering, and operational playbooks. You should not propose it by reflex. Propose it only when the availability target, business impact, or geographic footprint justifies the complexity.",
    ),
    QuestionAnswer(
        slug="disaster-recovery",
        category="availability",
        difficulty="medium",
        question="What do RPO and RTO mean in disaster recovery?",
        short_answer="RPO is the maximum acceptable data loss window. RTO is the maximum acceptable recovery time after a major failure.",
        deep_dive="These terms turn vague disaster-recovery claims into measurable objectives. If RPO is near zero, the system needs strong replication or synchronous commits. If RTO must be minutes, restore automation, standby infrastructure, and failover procedures matter. Good answers tie the backup and replication strategy directly to these targets.",
    ),
    QuestionAnswer(
        slug="api-versioning",
        category="api-design",
        difficulty="medium",
        question="When should you version an API?",
        short_answer="When you need to make incompatible contract changes that existing clients cannot absorb safely.",
        deep_dive="Versioning is often overused. If you can evolve a contract compatibly by adding optional fields or supporting old and new semantics simultaneously, do that first. When versioning is necessary, explain how old clients are migrated and how long compatibility is maintained.",
    ),
    QuestionAnswer(
        slug="pagination",
        category="api-design",
        difficulty="easy",
        question="Why is pagination important in API design?",
        short_answer="It prevents expensive unbounded reads, controls response size, and makes latency and memory usage more predictable.",
        deep_dive="Offset pagination is simple but can become slow or inconsistent at scale. Cursor or keyset pagination is often better for large ordered datasets because it aligns with indexes and avoids scanning. Mention consistency, duplicate/missing entries across pages, and how clients resume reads.",
    ),
    QuestionAnswer(
        slug="websocket-vs-polling",
        category="realtime",
        difficulty="medium",
        question="When should you choose WebSockets over polling?",
        short_answer="Use WebSockets when you need low-latency bidirectional updates. Use polling or long polling when update frequency is low or operational simplicity matters more.",
        deep_dive="Real-time transport choices should follow product needs. WebSockets add connection lifecycle management, fanout infrastructure, and state tracking. Polling is simpler and often sufficient for dashboards, low-frequency notifications, or internal tools. Strong answers compare freshness requirements, fanout, scale, and cost.",
    ),
    QuestionAnswer(
        slug="search-system-basics",
        category="search",
        difficulty="medium",
        question="Why do many products use a search index instead of querying the primary database directly for text search?",
        short_answer="Because full-text search, ranking, tokenization, and fuzzy matching are specialized workloads that general OLTP databases do not handle as efficiently.",
        deep_dive="Search systems optimize for inverted indexes, analyzers, ranking, and relevance. Primary databases optimize for transactional integrity. A good system design answer separates the source of truth from the search index and explains how indexing lag and reindexing are handled.",
    ),
    QuestionAnswer(
        slug="feed-generation",
        category="product-patterns",
        difficulty="hard",
        question="What is the tradeoff between fanout-on-write and fanout-on-read for feed generation?",
        short_answer="Fanout-on-write precomputes feeds for faster reads but makes writes heavier. Fanout-on-read computes feeds at read time, making writes simpler but reads slower and more expensive.",
        deep_dive="This is a classic design tradeoff for social timelines and notification systems. Fanout-on-write works well when read traffic dominates and follower counts are moderate. Fanout-on-read helps with celebrities or very large fanout because precomputing every update is too expensive. Many real systems use a hybrid approach.",
    ),
    QuestionAnswer(
        slug="leader-election",
        category="coordination",
        difficulty="hard",
        question="Why do distributed systems need leader election?",
        short_answer="Leader election allows one node to coordinate tasks like scheduling, failover control, metadata updates, or partition assignment to avoid conflicting actions.",
        deep_dive="Without coordination, multiple nodes can attempt the same exclusive action, causing corruption or duplicated work. Systems such as ZooKeeper, etcd, or built-in consensus services are used to manage leadership. Strong answers mention failure detection, leases, and split-brain prevention.",
    ),
    QuestionAnswer(
        slug="consensus-basics",
        category="coordination",
        difficulty="hard",
        question="What problem do consensus protocols like Raft or Paxos solve?",
        short_answer="They let distributed nodes agree on a sequence of decisions even when some nodes fail, enabling consistent metadata or replicated state machines.",
        deep_dive="Consensus matters when correctness of shared state is more important than raw latency. It is commonly used for cluster metadata, leader election, configuration, and strongly consistent storage primitives. In interviews, mention that consensus is expensive and should not be introduced unless the problem truly requires it.",
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
    sections = ["# System Design Question Bank", ""]
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
