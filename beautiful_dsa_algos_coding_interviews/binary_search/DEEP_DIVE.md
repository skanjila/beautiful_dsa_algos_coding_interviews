# Binary Search Deep Dive

Binary search works by halving the search space whenever the current midpoint
reveals which half can be discarded.

## Interview Approach

Use binary search when all of these are true:

- the search space is ordered or can be made monotonic
- a midpoint decision lets you discard half the possibilities
- you only need one boundary, one position, or one threshold

Stay calm by saying the invariant out loud. For example:

- left side is definitely too small
- right side is definitely too large
- answer is still inside `[left, right]`

That prevents pointer mistakes and makes your reasoning easier to defend.

## `search_insert`

Returns the existing index of a target or the insertion point that preserves sort order.

- Core invariant: everything before `left` is `< target`, everything after
  `right` is `>= target`.
- Pattern to use quickly: boundary-finding binary search.
- Big O: `O(log N)` time because each midpoint check throws away half of the
  remaining array, so the number of iterations grows with how many times `N`
  can be halved. Space stays `O(1)` because only a few index variables are kept.

## `find_first_and_last_position`

Uses two binary searches to find the first and last occurrence of a target.

- `_binary_boundary`: one search for the left boundary or right boundary.
- `search_range`: runs the boundary search twice.
- Pattern to use quickly: repeated boundary search.
- Big O: `O(log N)` time because each of the two boundary searches is still a
  normal binary search over the same array, so you do roughly `2 * log N`
  midpoint checks, which simplifies to `O(log N)`. Space stays `O(1)`.

## `search_in_rotated_array`

Searches a sorted array that has been rotated around a pivot.

- Core insight: even after rotation, at least one half around `mid` remains sorted.
- Use that sorted half to decide whether the target is inside or outside it.
- Pattern to use quickly: modified binary search on partially ordered data.
- Big O: `O(log N)` time because even though the array is rotated, every step
  still discards one entire half after checking which side is sorted. Space is
  `O(1)` because no auxiliary structure is built.

## `median_of_two_sorted_arrays`

Current implementation merges both arrays, then reads the middle.

- Simpler than the optimal partition-based solution.
- Pattern to use quickly: merge-two-sorted-lists thinking first, optimize later.
- Big O: `O(M + N)` time because the merge touches each element from both input
  arrays once. Space is also `O(M + N)` because the current implementation
  materializes the merged array instead of partitioning in place.

## Edge-case wrappers

- `search_insert_edge_cases`
- `find_first_and_last_position_edge_cases`
- `search_in_rotated_array_edge_cases`
- `median_of_two_sorted_arrays_edge_cases`

These wrappers make behaviors like empty arrays, singleton arrays, out-of-range
targets, and duplicate-heavy rotated arrays explicit. In the general case they
preserve the same asymptotic complexity as the wrapped function.
