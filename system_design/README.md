# System Design Study Guide

This directory is a study-focused system design submodule. It gives you two
things:

- a large interview-style Q&A bank you can drill repeatedly
- a structured Python representation that the test suite validates

It also now includes small runnable reference implementations under
[implementations](implementations/) for concepts that come up repeatedly in
interviews, such as rate limiting and Kafka-style event buses.

If you want the raw structured source, see [question_bank.py](question_bank.py).

## How To Study

1. Start with fundamentals and scaling.
2. Move to data, caching, and messaging.
3. Rehearse reliability, observability, and security answers out loud.
4. Use the product-pattern questions to practice end-to-end tradeoff thinking.

## Categories

- fundamentals
- scaling
- data
- caching
- messaging
- reliability
- observability
- security
- availability
- api-design
- realtime
- search
- coordination
- product-patterns

## High-Value Interview Questions And Answers

### What is the difference between functional and non-functional requirements?

Functional requirements define what the system does. Non-functional
requirements define the operating constraints, such as latency, throughput,
availability, durability, security, or cost.

Deep dive:
Start every design by separating user-visible capabilities from system-quality
targets. This keeps the rest of the design grounded because every component
choice can be traced back to a constraint.

### Why do rough scale estimations matter?

Because scale drives architecture. A service handling a few hundred requests per
minute can stay simple; a service handling millions of requests per second
cannot.

Deep dive:
Estimate read QPS, write QPS, storage growth, object size, and burst factor.
Even approximate numbers are enough to decide whether you need caching,
partitioning, asynchronous pipelines, or global distribution.

### What problem does a load balancer solve?

It distributes traffic across service instances and shields clients from backend
topology changes.

Deep dive:
A load balancer also enables health checks, TLS termination, rolling deploys,
and traffic shaping. Good answers mention that load balancers themselves must be
redundant because they are critical infrastructure.

### Why are stateless services easier to scale?

Because any instance can process any request when state is stored elsewhere.

Deep dive:
Stateless services simplify autoscaling, restarts, blue-green deploys, and
regional failover. If state must exist, describe clearly where it lives and how
it survives instance loss.

### When would you choose SQL over NoSQL?

Choose SQL when transactional integrity, joins, and strong consistency dominate.
Choose NoSQL when workload shape or scale characteristics favor partitioned
access patterns, denormalization, or flexible schemas.

Deep dive:
Do not answer this ideologically. Connect the storage choice directly to access
patterns, transactional guarantees, and operational tradeoffs.

### What is sharding and what problems does it introduce?

Sharding partitions data across multiple nodes so one machine is no longer the
bottleneck.

Deep dive:
Sharding introduces routing logic, hot partitions, rebalancing, and cross-shard
query complexity. A strong answer always mentions the shard key and why it fits
the dominant access paths.

### Why do systems add caches?

Caches reduce latency and lower load on databases or services by serving
repeated reads from faster storage.

Deep dive:
Caching only works when you can define keys, freshness rules, and miss behavior.
Without an invalidation strategy, the cache becomes a correctness liability.

### What is the cache-aside pattern?

The application checks cache first, then falls back to the database on a miss,
then populates the cache.

Deep dive:
This pattern is simple and common, but you should call out stale data,
thundering herd behavior, and negative caching for not-found lookups.

### When do you introduce a message queue?

When work can be decoupled from the request path or when producers and consumers
operate at different rates.

Deep dive:
Queues help with burst absorption and failure isolation, but they require retry
policy, dead-letter handling, ordering decisions, and idempotent consumers.

### Why is idempotency important?

Because retries are inevitable in distributed systems, and operations must be
safe when repeated.

Deep dive:
Without idempotency, network retries can cause duplicate charges, duplicate
notifications, and inconsistent state transitions. Mention keys, dedupe tables,
and natural uniqueness constraints.

### What does graceful degradation mean?

It means preserving the core experience by dropping or simplifying non-critical
features during overload or dependency failure.

Deep dive:
Examples include serving cached recommendations, disabling expensive ranking,
and delaying analytics writes. This is a product decision as much as an
infrastructure pattern.

### What are the three observability pillars?

Logs, metrics, and traces.

Deep dive:
Metrics tell you that something is wrong, logs help explain a local event, and
traces show where time was spent across service boundaries.

### What are the basic security concerns in service design?

Authentication, authorization, input validation, transport security, secret
management, auditability, and abuse prevention.

Deep dive:
A strong security answer is specific about where identity is established, how
authorization is enforced, and how sensitive data is handled end to end.

### Why deploy across multiple regions?

To improve global latency and survive regional outages.

Deep dive:
Multi-region design is expensive and should be justified. It complicates data
replication, failover, operational playbooks, and consistency behavior.

### What is the tradeoff between fanout-on-write and fanout-on-read?

Fanout-on-write makes reads fast by precomputing feed data, but it increases
write amplification. Fanout-on-read keeps writes lighter but makes reads more
expensive.

Deep dive:
This is a classic social feed question. The best answers discuss hybrid
strategies for users with very high follower counts and tie the choice to read
versus write ratios.

## Deep-Dive Areas To Rehearse

- Do rough math before drawing boxes.
- Say who owns each write path.
- Explain read path versus write path separately.
- Be explicit about failure modes.
- Tie every scaling mechanism to a real bottleneck.
- Mention observability and operational recovery before closing.

## Suggested Practice Routine

- Day 1: fundamentals, scaling, capacity planning
- Day 2: data, replication, consistency, partitioning
- Day 3: caching, messaging, asynchronous workflows
- Day 4: reliability, observability, security
- Day 5: product patterns such as feeds, search, and realtime updates
- Day 6: full interview walk-throughs on one product at a time

## Programmatic Access

The question bank is intentionally structured so you can inspect it in Python:

```python
from system_design.question_bank import list_categories, search_questions

print(list_categories())
for item in search_questions("cache"):
    print(item.question)
```
