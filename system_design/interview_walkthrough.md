# System Design Interview Walkthrough

## Default Answer Structure

Use this sequence repeatedly until it becomes automatic:

1. Clarify functional requirements.
2. Clarify non-functional requirements.
3. Estimate scale roughly.
4. Identify core APIs and data entities.
5. Walk the write path.
6. Walk the read path.
7. Identify bottlenecks and scaling levers.
8. Add reliability, observability, and security.
9. Close with tradeoffs and future improvements.

## Questions To Ask Early

- Who are the users?
- What is the primary use case?
- What is the expected read/write ratio?
- What consistency guarantees actually matter?
- What is the traffic shape: average, peak, burst?
- What data retention period is required?
- Is this globally distributed or region-local?
- Is the system latency-sensitive or throughput-sensitive?

## Common Follow-Up Questions

### How would you handle a sudden traffic spike?

Use edge rate limiting, elastic stateless services, caches for hot reads, and
queues for non-critical async work. Then explain what still remains stateful and
how that layer is protected.

### How would you avoid a single database bottleneck?

Start with indexing and caching. Then add replicas for reads, partitioning for
writes or storage growth, and asynchronous pipelines for work that does not need
to stay synchronous.

### What would you monitor first in production?

Request rate, error rate, latency percentiles, dependency health, queue lag, DB
latency, cache hit rate, and saturation signals such as CPU, memory, and
connection pool exhaustion.

### What tradeoff did your design make?

Name one clearly. For example:

- we chose eventual consistency for timelines to improve write scalability
- we accepted stale cache reads for lower latency
- we kept the first version single-region to reduce operational complexity

## Practice Prompts

- Design a URL shortener.
- Design a rate limiter.
- Design a chat system.
- Design a social feed.
- Design a notification platform.
- Design an order service.
- Design a file storage service.
- Design a search autocomplete service.
