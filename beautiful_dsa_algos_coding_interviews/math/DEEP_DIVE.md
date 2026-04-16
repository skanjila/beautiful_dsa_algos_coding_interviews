# Math Deep Dive

This directory currently contains matrix transformation problems.

## Interview Approach

For matrix problems, slow down and ask:

- is this an index-mapping problem?
- is the output grouped by a formula like `r + c` or `r - c`?
- can the transformation be done in place?

In interviews, drawing a `3 x 3` example usually reveals the pattern faster
than abstract reasoning.

## `matrix_antidiagonals`

Groups matrix values by `row + column`.

- Every cell with the same `r + c` belongs to the same anti-diagonal.
- Pattern to use quickly: coordinate-grouping by invariant.
- Big O: `O(R * C)` time, `O(R * C)` space for the grouped output.

## `matrix_rotation`

Rotates an `N x N` matrix 90 degrees clockwise in place.

- Phase 1: transpose across the main diagonal.
- Phase 2: reverse each row.
- Pattern to use quickly: decompose one complex transform into two simpler transforms.
- Big O: `O(N^2)` time, `O(1)` auxiliary space.

## `edge_cases`

Wrapper functions make behavior for empty inputs explicit while preserving the
same asymptotic complexity as the underlying implementation.
