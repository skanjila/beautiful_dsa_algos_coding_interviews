# REST Best Practices

## Goal

Use REST when the problem is naturally resource-oriented, HTTP semantics are
useful, and broad client compatibility matters more than a highly optimized
binary contract.

## When REST Is a Good Fit

- public APIs consumed by browsers, mobile clients, or third parties
- CRUD-heavy service boundaries
- systems where caching, proxies, and HTTP tooling are useful
- teams that value debuggability with plain text payloads

REST is often the default because most engineers, tools, and observability
stacks already understand HTTP well.

## Core Principles

- Model stable resources, not controller methods.
- Let HTTP methods carry meaning instead of inventing custom verbs everywhere.
- Keep request and response shapes explicit and predictable.
- Design endpoints around client use cases, not only around database tables.
- Use consistent error shapes and status codes.

## Resource Modeling

Good resource names are nouns:

- `GET /users/{user_id}`
- `POST /orders`
- `PATCH /profiles/{profile_id}`

Avoid RPC-style endpoint sprawl unless the action is truly not a normal
resource change:

- better: `POST /orders`
- acceptable for action semantics: `POST /payments/{payment_id}:capture`

If you use action endpoints, keep them rare and easy to justify.

## HTTP Method Semantics

- `GET` reads data and should not mutate state.
- `POST` creates a resource or triggers a non-idempotent action.
- `PUT` replaces the full resource representation.
- `PATCH` partially updates a resource.
- `DELETE` removes a resource or marks it deleted.

In interviews, call out idempotency:

- `GET`, `PUT`, and `DELETE` are expected to be idempotent
- `POST` usually is not unless you add an idempotency key

That matters because retries are common in distributed systems.

## URL Design

- keep URLs short and resource-based
- use plural nouns consistently
- use nested paths only when the ownership relationship is strong
- avoid deeply nested URLs that mirror every join in the database

Reasonable:

- `/users/{user_id}/orders`

Usually too deep:

- `/companies/{company_id}/departments/{department_id}/teams/{team_id}/users/{user_id}/orders`

Long nesting makes APIs harder to reason about and often exposes internal data
relationships the client does not actually need.

## Request and Response Design

- Validate input at the boundary.
- Return typed fields instead of overloading strings.
- Keep naming consistent across endpoints.
- Prefer explicit pagination fields over ad hoc list slicing.

Typical list response:

```json
{
  "items": [],
  "next_cursor": "abc123"
}
```

Prefer cursor pagination for large or changing datasets. Offset pagination is
easy to start with, but it becomes less reliable when rows are inserted or
deleted during traversal.

## Status Codes

Use a small, predictable set well:

- `200 OK` for normal reads and updates
- `201 Created` for successful creates
- `202 Accepted` for async work
- `204 No Content` when there is nothing useful to return
- `400 Bad Request` for malformed requests
- `401 Unauthorized` when authentication is missing or invalid
- `403 Forbidden` when the caller is authenticated but not allowed
- `404 Not Found` when the resource does not exist
- `409 Conflict` for version or state conflicts
- `422 Unprocessable Entity` for semantically invalid input
- `429 Too Many Requests` for rate limiting
- `500` / `502` / `503` / `504` for server and dependency failures

The important thing is not memorizing every code. The important thing is using
them consistently so clients can automate behavior.

## Error Design

Return errors in a stable, machine-readable shape:

```json
{
  "code": "validation_error",
  "message": "email is required",
  "details": {
    "field": "email"
  }
}
```

Best practice:

- `code` is stable for machines
- `message` is readable for humans
- `details` carries structured context

Avoid making clients parse free-form text to understand failures.

## Versioning and Evolution

Prefer backward-compatible changes first:

- add optional fields
- add new endpoints
- relax validation when safe

Use explicit versioning only when compatibility cannot be maintained. Common
choices:

- URI versioning: `/v1/users`
- header-based versioning

URI versioning is easier to explain and operate in interviews, even if some
teams prefer headers.

## Idempotency, Retries, and Timeouts

For client-facing write APIs:

- support idempotency keys where retries may create duplicates
- set timeouts on downstream calls
- retry only transient failures
- avoid blind retries on validation or conflict errors

Example:

- creating a payment with `POST /payments`
- client sends `Idempotency-Key`
- server stores the key and result
- retry returns the same logical outcome instead of double-charging

## Caching

REST works well with HTTP caching when reads dominate:

- use `Cache-Control` intentionally
- use `ETag` or `Last-Modified` when validation caching helps
- know which responses must never be cached

This is one of REST's practical strengths over many RPC interfaces.

## Concurrency Control

When lost updates matter, say so explicitly:

- optimistic locking with version numbers
- conditional writes with `ETag` / `If-Match`

This is a strong interview signal because many candidates stop at basic CRUD and
never explain how concurrent writes stay correct.

## Security

- authenticate every request
- authorize at the use-case level, not only at the router
- validate and sanitize input
- avoid exposing internal-only identifiers when public IDs are better
- use TLS everywhere

## Observability

At minimum:

- request ID or trace ID
- structured logs
- latency, throughput, and error metrics
- dependency-level visibility

Helpful metrics:

- p50 / p95 / p99 latency by endpoint
- error rate by status code family
- rate-limit rejections
- cache hit rate

## Testing

- unit tests for serializers, validators, and business logic
- integration tests for database and external dependencies
- contract tests for request and response compatibility
- end-to-end tests only for critical flows

## Common Interview Mistakes

- describing controllers instead of resources
- using `POST` for everything
- ignoring idempotency and retries
- returning inconsistent error shapes
- skipping pagination and filtering
- forgetting auth, rate limiting, and observability

## Interview Framing

When asked whether to use REST, structure your answer like this:

1. Explain why the domain is resource-oriented.
2. Name the core resources and endpoints.
3. Describe request and response structure.
4. Cover pagination, errors, idempotency, and versioning.
5. Add reliability, security, and observability.
6. State when gRPC or messaging would be a better fit.

## REST vs gRPC in One Sentence

Choose REST when readability, compatibility, and HTTP-native tooling matter
most. Choose gRPC when strict contracts, low latency, and service-to-service
efficiency matter most.
