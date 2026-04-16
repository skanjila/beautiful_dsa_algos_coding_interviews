# Rate Limiting Algorithms And Kafka-Style FIFO Event Bus

## Why These Two Topics Matter

These are common system design interview topics because they force you to talk
about control, fairness, scaling, and failure handling.

- rate limiting protects downstream systems from overload and abuse
- an event bus decouples producers from consumers and absorbs bursty traffic

They also show up together in real systems. For example:

- an API gateway rate limits client requests
- accepted requests publish events to a bus
- consumers process those events asynchronously

## Rate Limiting Goals

Rate limiting is usually introduced to answer one or more of these questions:

- how do we stop a single client from overwhelming the service
- how do we protect expensive dependencies
- how do we enforce quotas by user, API key, tenant, or region
- how do we shape traffic instead of simply dropping everything

In interviews, say what the limiter key is. A rate limiter without a clear key
such as `user_id`, `api_key`, or `IP` is underspecified.

## Fixed Window Counter

Idea:

- group requests into discrete windows such as one minute
- count how many requests happen in that window
- reject requests after the limit is reached

Example:

- limit: `100 requests per minute`
- user sends `100` requests at `12:00:59`
- user sends `100` more at `12:01:00`

That user just sent `200` requests in about one second, even though the limiter
technically respected the per-minute rule.

Strengths:

- very easy to implement
- low memory overhead
- good first answer in interviews

Weaknesses:

- bursty near window boundaries
- fairness is only approximate

When to use it:

- simple quota enforcement
- low-cost internal protection
- first-pass design before discussing more precise algorithms

## Sliding Window Log

Idea:

- store timestamps of recent requests
- remove timestamps older than the active window
- allow the new request only if the remaining count is below the limit

Why it is better:

- the active window moves continuously
- avoids the large burst at fixed-window boundaries

Tradeoff:

- more precise
- more memory because each request timestamp is stored

When to use it:

- stricter fairness requirements
- smaller traffic volume per key
- cases where exactness matters more than memory efficiency

## Sliding Window Counter

Idea:

- approximate a sliding window by combining counts from the current window and
  the previous window
- weight the previous window based on how far into the current window you are

Why people use it:

- cheaper than storing every timestamp
- more accurate than a fixed window

Interview note:

You do not always need to implement this in code, but you should know where it
fits in the tradeoff ladder:

- fixed window: simplest
- sliding window counter: middle ground
- sliding window log: most precise of the common counter-based answers

## Token Bucket

Idea:

- tokens refill at a steady rate
- each request consumes one or more tokens
- requests are allowed while tokens remain

Why it is useful:

- supports short bursts without losing control of the long-term average rate
- models many real API limits well

Example:

- bucket capacity: `20`
- refill rate: `5 tokens per second`
- a burst of `20` requests can pass immediately
- after that, traffic is limited by refill speed

When to use it:

- public APIs
- gateway enforcement
- traffic shaping where bursts are acceptable

## Leaky Bucket

Idea:

- requests enter a bucket or queue
- work leaves at a fixed rate

Why it matters:

- smooths traffic aggressively
- useful when downstream capacity is very predictable

Difference from token bucket:

- token bucket allows bursts up to capacity
- leaky bucket emphasizes steady output rate

## How To Answer Rate Limiting In An Interview

Use this order:

1. define the key: user, API key, tenant, IP, or endpoint
2. define the limit: requests per second, minute, or day
3. decide whether you need fairness or just coarse protection
4. choose the algorithm
5. explain where the state lives
6. explain what happens on rejection

Strong follow-up points:

- global rate limiting usually needs shared state such as Redis
- local in-memory rate limiting is simpler but only per-instance
- returning `429 Too Many Requests` is standard for HTTP APIs
- include retry behavior and observability

## Practical Implementation In This Repo

See:

- [implementations/rate_limiter.py](implementations/rate_limiter.py)

Included algorithms:

- `FixedWindowRateLimiter`
- `SlidingWindowLogRateLimiter`
- `TokenBucketRateLimiter`

These are intentionally small reference implementations. They are useful for
interview discussion because they make the tradeoffs easy to explain.

## What A Kafka-Style FIFO Event Bus Really Means

Kafka is not a single global FIFO queue.

The important correction is:

- ordering is guaranteed within a partition
- ordering is not guaranteed across all partitions of a topic

So if an interviewer says "Kafka-like FIFO queue," the precise answer is:

- it behaves like an append-only ordered log per partition
- consumers read records in offset order within each partition

This is one of the most important distinctions to explain clearly.

## Core Pieces Of A Kafka-Like Bus

1. Topic
   Logical stream of events.
2. Partition
   Ordered append-only log inside a topic.
3. Offset
   Position of a record inside a partition log.
4. Producer
   Writes events to a topic.
5. Consumer group
   Reads events and tracks progress with offsets.

If messages with the same key must stay ordered, they should route to the same
partition.

## Why Partitioning Exists

A single FIFO queue is easy to reason about but hard to scale.

Partitioning solves that by allowing:

- more write throughput
- more read parallelism
- smaller per-node bottlenecks

The cost is that total ordering disappears. You keep order only inside each
partition.

## How To Implement A Simple FIFO Event Bus

At interview scale, the design is:

- each topic has multiple partitions
- each partition is an append-only list
- each record gets the next offset in that partition
- a consumer group stores the next offset it should read

Why offsets matter:

- consumers can resume after failure
- replay becomes possible
- lag can be measured

This is different from a destructive queue where a message disappears as soon as
one consumer reads it.

## Practical Implementation In This Repo

See:

- [implementations/fifo_event_bus.py](implementations/fifo_event_bus.py)

Included concepts:

- topic creation
- partitioned appends
- deterministic key-to-partition mapping
- ordered offsets inside each partition
- consumer-group polling
- explicit offset commit
- lag calculation

This implementation is deliberately small, but it covers the mental model that
matters in interviews.

## Event Bus vs Traditional Queue

Traditional queue:

- one consumer usually removes the message
- replay is not a first-class concept
- ordering is often global or simpler

Kafka-style event bus:

- records stay in the log
- different consumer groups can read independently
- offsets let consumers replay or recover
- ordering is partition-scoped

## How To Answer Event Bus Questions In An Interview

Use this order:

1. state whether ordering must be global or partition-level
2. decide how producers choose partitions
3. explain offset tracking
4. explain replay and consumer recovery
5. explain lag and backpressure
6. explain dead-letter or retry handling if processing fails

Good follow-up points:

- key-based partitioning preserves per-entity order
- hot keys can create hot partitions
- exactly-once delivery is expensive and usually narrowed to specific scopes
- at-least-once plus idempotent consumers is more common

## Common Interview Mistakes

- saying Kafka gives global FIFO across the whole topic
- skipping the limiter key in rate-limiting discussions
- choosing an algorithm without discussing state placement
- forgetting retry behavior and idempotency
- confusing offsets with message IDs
- ignoring backpressure and consumer lag

## Suggested Practice

1. Explain fixed window, sliding window log, and token bucket out loud.
2. Implement one limiter from memory.
3. Explain why Kafka ordering is per partition.
4. Walk through producer write, consumer poll, offset commit, and replay.
5. Compare a queue, a log, and a streaming system in plain English.
