# Service Design

## Goal

Design services so that business logic, contracts, data access, and operations
concerns stay separable. A good service is easy to evolve, observable in
production, and boring to operate.

## Core Principles

- Keep APIs explicit: define request and response contracts first.
- Keep business logic in application services, not controllers or handlers.
- Make data ownership clear: one service should own each write model.
- Prefer idempotent operations where retries are likely.
- Design for failure: timeouts, retries, circuit breaking, and backpressure are
  not optional.
- Make observability part of the design, not an afterthought.

## Service Shape

Typical layers:

1. Transport layer
   HTTP, gRPC, messaging consumer, or scheduled trigger.
2. Application layer
   Orchestrates use cases and transactions.
3. Domain layer
   Business rules, invariants, and decision logic.
4. Infrastructure layer
   Database, cache, queue, external client, file system.

This separation keeps interview-scale code and production-scale code aligned.

## API Design

- Use resource-oriented naming for CRUD-like flows.
- Use action-oriented endpoints only when the operation is not naturally a
  resource mutation.
- Version only when contract evolution cannot be handled compatibly.
- Validate inputs at the boundary.
- Return stable error shapes with machine-readable codes.

Example error envelope:

```json
{
  "code": "validation_error",
  "message": "email is required",
  "details": {
    "field": "email"
  }
}
```

## Data Design

- Start with the access patterns, not the schema aesthetic.
- Normalize transactional data when integrity matters.
- Denormalize read models when latency matters.
- Store event timestamps consistently in UTC.
- Add indexes for real query paths, not hypothetical ones.

## Reliability Patterns

- Timeouts on all outbound calls.
- Retries only for transient failures.
- Idempotency keys for write endpoints exposed to clients.
- Dead-letter handling for asynchronous failures.
- Bulkheads or worker isolation for noisy dependencies.

## Asynchronous Design

Use queues or event streams when:

- work is slow or bursty
- the caller does not need the final result immediately
- side effects can be decoupled

Keep event contracts versioned and small. Prefer publishing facts like
`order_created` instead of commands like `send_email`.

## Security

- Authenticate every request.
- Authorize at the use-case boundary.
- Avoid leaking internal identifiers if public IDs are needed.
- Encrypt secrets and do not hardcode configuration.
- Log security-relevant actions with actor and target context.

## Observability

At minimum:

- structured logs
- request IDs / trace IDs
- latency, throughput, error rate metrics
- health and readiness checks

Useful default metrics:

- request count
- p95 / p99 latency
- dependency failure count
- DB query latency
- queue lag

## Testing Strategy

- Unit tests for domain logic and pure transformation code.
- Integration tests for DB and external client boundaries.
- Contract tests for external APIs or event payloads.
- End-to-end tests only for critical paths.

## Interview Framing

When asked to design a service, structure the answer in this order:

1. Clarify requirements and scale.
2. Define the API contract.
3. Identify core entities and ownership.
4. Walk through write path and read path.
5. Add failure handling, scaling, and observability.
6. Call out tradeoffs and future evolution.
