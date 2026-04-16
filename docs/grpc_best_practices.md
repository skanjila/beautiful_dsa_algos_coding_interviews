# gRPC Best Practices

## Goal

Use gRPC when you want strong contracts, efficient service-to-service
communication, and explicit API evolution rules across internal systems.

## When gRPC Is a Good Fit

- internal microservice communication
- latency-sensitive service calls
- polyglot backends that benefit from generated clients
- streaming use cases
- systems where schema discipline matters

gRPC is usually less convenient than REST for broad public consumption, but it
is often a better fit for internal platforms where performance and contract
clarity matter more than human readability.

## Core Principles

- design the protobuf contract first
- treat field numbers as part of the public contract
- keep messages small and purpose-built
- model backward-compatible evolution deliberately
- propagate deadlines, cancellation, and tracing metadata

## Service Design

Prefer use-case oriented RPCs over blindly mapping every database table into a
service.

Good:

- `GetUser`
- `ListOrders`
- `CreatePayment`
- `StreamNotifications`

Weak design:

- `DoOperation1`
- `ExecuteThing`

Names should tell the caller what business capability they are invoking.

## Message Design

- use explicit message types for requests and responses
- avoid giant "god messages" with many unrelated optional fields
- use repeated fields for collections
- document units, currency, timestamps, and enum meaning clearly

Bad message design usually shows up as unclear ownership and constant schema
churn.

## Field Number Discipline

In protobuf, field numbers matter because the binary wire format depends on
them.

That means:

- never reuse old field numbers
- reserve removed field numbers
- reserve removed field names when helpful

This is one of the easiest ways to break compatibility if the team is careless.

## Backward Compatibility

Safe changes usually include:

- adding new optional fields
- adding new RPC methods
- adding new enum values carefully

Risky or breaking changes include:

- reusing field numbers
- changing field meaning without changing the contract
- changing a singular field into a semantically incompatible shape

In interviews, say that old clients and new servers must continue to interoperate
through controlled schema evolution.

## Error Handling

Use gRPC status codes intentionally:

- `INVALID_ARGUMENT`
- `NOT_FOUND`
- `ALREADY_EXISTS`
- `FAILED_PRECONDITION`
- `UNAUTHENTICATED`
- `PERMISSION_DENIED`
- `RESOURCE_EXHAUSTED`
- `UNAVAILABLE`
- `DEADLINE_EXCEEDED`

These should map to clear client behavior:

- retry transient failures
- do not retry validation failures
- surface auth problems clearly

Avoid encoding every failure as a successful response with an error field. That
throws away the transport's native semantics.

## Deadlines, Timeouts, and Retries

Deadlines are essential in gRPC systems.

- callers should send deadlines
- servers should respect cancellation
- downstream calls should not outlive the upstream request budget

Without deadlines, slow dependency chains can pile up and exhaust threads or
connection pools.

Retries should be selective:

- retry `UNAVAILABLE` or some network failures
- do not retry invalid input or permission failures
- require idempotency for retried writes

## Streaming

gRPC supports:

- unary RPCs
- server streaming
- client streaming
- bidirectional streaming

Use streaming when it matches the problem:

- large result sets
- event delivery
- incremental progress updates

Do not use streaming just because it exists. Unary RPCs are easier to operate
and debug when the use case is simple.

## Metadata

Use metadata for:

- auth tokens
- request IDs / trace IDs
- tenant or routing context where appropriate

Do not overload metadata with core business fields that belong in the request
message itself.

## API Granularity

Too chatty:

- many tiny RPCs that require several network round trips to do one task

Too coarse:

- one huge RPC that returns everything and becomes impossible to evolve

Aim for use-case-sized RPCs that match real workflows.

## Security

- use TLS for transport security
- authenticate callers, often with mTLS or token-based auth
- authorize at the business-operation layer
- validate input even for internal services

Internal does not mean trusted.

## Observability

At minimum:

- request volume
- latency percentiles
- error rate by status code
- deadline exceeded count
- retry count
- per-method metrics

Also propagate tracing context so you can follow a call across service
boundaries.

## Load Shedding and Reliability

- enforce deadlines
- bound concurrency
- shed excess traffic when needed
- use circuit breaking or fail-fast behavior for unhealthy dependencies

Because gRPC is often used deep inside service graphs, small reliability
mistakes can amplify quickly.

## Contract Ownership

Every proto should have clear ownership:

- who can change it
- how changes are reviewed
- how client compatibility is checked

Shared proto packages without ownership often decay into confusing, unstable
interfaces.

## Testing

- unit tests for business logic behind handlers
- contract tests for proto evolution
- integration tests for client/server interoperability
- load tests for high-throughput or streaming paths

Generated clients make contract testing especially valuable.

## Common Interview Mistakes

- treating gRPC as "REST but faster"
- ignoring deadlines and cancellation
- forgetting schema evolution rules
- making RPCs too chatty
- skipping status-code design
- ignoring observability and retries

## Interview Framing

When asked whether to use gRPC, structure your answer like this:

1. Explain why the communication is internal and contract-heavy.
2. Describe the key RPCs and protobuf messages.
3. Explain compatibility rules and schema evolution.
4. Cover deadlines, retries, idempotency, and status codes.
5. Add auth, tracing, and metrics.
6. State when REST would still be the better choice.

## gRPC vs REST in One Sentence

Choose gRPC when contract rigor, streaming, and service-to-service efficiency
matter most. Choose REST when human readability, broad compatibility, and
HTTP-native behavior matter most.
