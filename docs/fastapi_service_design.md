# FastAPI Service Design

## Goal

Use FastAPI to keep route handlers thin, service functions testable, schemas
explicit, and async boundaries intentional.

## Recommended Project Structure

```text
app/
  api/
    routes/
  services/
  repositories/
  models/
  schemas/
  clients/
  core/
  db/
  dependencies/
  main.py
```

For larger systems, prefer feature-first modules:

```text
app/orders/
  router.py
  service.py
  repository.py
  schemas.py
  models.py
```

## Layer Responsibilities

- FastAPI route handlers: parse input, invoke service, map errors to HTTP.
- service layer: use-case orchestration and business rules.
- repository layer: data access only.
- schemas: request and response contracts via Pydantic.
- models: persistence models, usually SQLAlchemy or SQLModel.

## Sync vs Async

- Use `async def` when the stack is truly async end to end.
- If DB/client libraries are synchronous, a fake async route gives little value.
- Do not block the event loop with CPU-heavy work; move that to workers.

## Schema Rules

- Use dedicated request and response models.
- Avoid returning raw ORM objects directly.
- Validate at the boundary with Pydantic.
- Keep internal fields out of public response schemas.

## Dependency Injection

Use FastAPI dependencies for:

- auth context
- DB session creation
- pagination parameters
- request-scoped services

Do not bury business logic inside dependency functions.

## Persistence

- Keep session lifecycle centralized.
- Commit in the service layer when the use case finishes.
- Roll back on exceptions.
- Write repository methods around access patterns, not generic CRUD abstractions
  that hide real queries.

## Error Handling

- Raise `HTTPException` only at the transport boundary.
- In service code, prefer domain exceptions.
- Map domain exceptions to HTTP responses in one place.

## Background Work

Use:

- `BackgroundTasks` for small, fire-and-forget local work
- Celery, RQ, Dramatiq, or a queue consumer for durable async jobs

Do not use in-process background tasks for critical business workflows.

## Observability

- structured logs
- request ID middleware
- metrics for request count, latency, and failures
- health and readiness endpoints
- tracing for DB and outbound HTTP if available

## Security

- Centralize authentication and authorization dependencies.
- Validate scopes or roles close to the route boundary.
- Never trust client-supplied identifiers for authorization decisions.

## Testing Strategy

- Unit test services directly.
- Use `TestClient` or `httpx.AsyncClient` for route tests.
- Use transactional test DB fixtures for repository tests.
- Mock external clients at the service boundary.

## Example Layout

```python
from fastapi import APIRouter, Depends
from app.orders.schemas import CreateOrderRequest, OrderResponse
from app.orders.service import OrderService
from app.dependencies import get_order_service

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse)
async def create_order(
    request: CreateOrderRequest,
    service: OrderService = Depends(get_order_service),
) -> OrderResponse:
    return await service.create_order(request)
```

## Default Production Checklist

- typed settings object
- startup/shutdown lifecycle hooks
- consistent exception handlers
- DB connection health checks
- request timeout strategy at proxy/load balancer
- metrics and structured logging
