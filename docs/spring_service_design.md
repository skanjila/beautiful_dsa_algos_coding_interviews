# Spring Service Design

## Goal

Use Spring to keep controllers thin, services cohesive, persistence explicit,
and operational concerns standardized.

## Recommended Package Structure

```text
src/main/java/com/example/app
  controller/
  service/
  domain/
  repository/
  client/
  config/
  dto/
  mapper/
  exception/
```

For larger systems, organize by feature instead of by layer:

```text
orders/
  OrderController.java
  OrderService.java
  OrderRepository.java
  OrderMapper.java
  dto/
```

## Layer Responsibilities

- `@RestController`: request parsing, validation, response mapping.
- `@Service`: orchestration, transactions, invariants, use-case logic.
- `@Repository`: persistence operations only.
- domain objects: business state and business rules.

Avoid placing business rules inside controllers or JPA entities by default.

## DTO and Entity Rules

- Do not expose JPA entities directly over the wire.
- Use request and response DTOs.
- Use mappers explicitly; keep them predictable.
- Keep persistence annotations out of transport models.

## Transactions

- Put `@Transactional` at the service layer.
- Use read-only transactions for query-only operations.
- Keep transactions short.
- Do not call slow external services inside DB transactions unless absolutely
  necessary.

## Persistence

- Use Spring Data JPA only where the relational model fits.
- Write explicit queries for non-trivial fetch patterns.
- Avoid N+1 problems with fetch joins or projections.
- Use optimistic locking for concurrent updates where correctness matters.

## Validation and Errors

- Use Bean Validation on request DTOs.
- Centralize exception handling with `@ControllerAdvice`.
- Return consistent error payloads and HTTP codes.

Example mapping:

- `400` invalid input
- `401` unauthenticated
- `403` unauthorized
- `404` not found
- `409` conflict
- `422` business rule violation
- `500` internal failure

## External Calls

- Wrap external dependencies in client classes.
- Apply timeouts and retries at the client boundary.
- Use circuit breakers where dependencies are unstable.
- Prefer `WebClient` for reactive/non-blocking flows.
- Use `RestClient` or `RestTemplate` only where simplicity is enough.

## Observability

- Use structured logs.
- Propagate correlation IDs.
- Expose Actuator endpoints.
- Publish Micrometer metrics.
- Trace outbound HTTP and DB spans when possible.

## Security

- Use Spring Security for authentication and authorization.
- Enforce method-level authorization for sensitive use cases.
- Keep JWT parsing and role mapping centralized.
- Do not mix security logic into controllers.

## Testing Strategy

- Unit test services with mocked repositories and clients.
- Use `@WebMvcTest` for controller slices.
- Use `@DataJpaTest` for repository behavior.
- Use a small number of `@SpringBootTest` integration tests for full wiring.

## Default Production Checklist

- health and readiness endpoints
- DB migration tool like Flyway or Liquibase
- explicit config profiles
- request timeout configuration
- standardized exception mapping
- metrics and log correlation

## Service Template

```java
@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final PaymentClient paymentClient;

    public OrderService(OrderRepository orderRepository, PaymentClient paymentClient) {
        this.orderRepository = orderRepository;
        this.paymentClient = paymentClient;
    }

    @Transactional
    public OrderResponse createOrder(CreateOrderRequest request) {
        // validate business rules
        // persist aggregate
        // trigger downstream work
        // map to response DTO
        return null;
    }
}
```
