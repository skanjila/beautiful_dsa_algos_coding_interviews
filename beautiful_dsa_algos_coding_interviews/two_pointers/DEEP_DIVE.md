# Two Pointers Deep Dive

Two-pointer problems move two indices through ordered or cleaned data while
maintaining an invariant.

## Interview Approach

Two pointers usually show up when:

- the data is sorted or can be sorted
- you need to compare pairs from both ends
- you need linear-time scanning without nested loops

The calm question to ask is: what invariant do the two pointers maintain?

## `is_palindrome`

Checks whether a cleaned alphanumeric-only string is symmetric.

- Build a normalized lowercase string.
- Compare characters from the left and right ends inward.
- Pattern to use quickly: symmetric inward scan.
- Big O: `O(N)` time because the string is scanned once to filter characters
  and then compared with two pointers in another linear pass. Space is `O(N)`
  because the cleaned version of the string is stored explicitly.

## `three_sum`

Finds unique triplets that sum to zero.

- Sort the array first.
- Fix one value and solve the remaining two-sum problem with left/right pointers.
- Skip duplicates at the fixed index and at both moving pointers.
- Pattern to use quickly: sort + fix one value + two-sum with two pointers.
- Big O: `O(N^2)` time because after sorting, the outer loop picks each first
  value once and the inner two-pointer sweep moves left/right across the rest
  of the array linearly for that choice. Auxiliary space is `O(1)` excluding
  output because the search reuses the sorted array in place.

## `three_sum_bf`

Brute-force reference for the same problem.

- Try every triplet combination.
- Use a set to deduplicate sorted triplets.
- Interview value: useful as a baseline before optimizing to the two-pointer solution.
- Big O: `O(N^3)` time because the brute-force version tries every triple of
  indices. Extra space is `O(K)` for the set or list of unique triplets that
  survive deduplication.

## `edge_cases`

Wrappers make null handling and too-short inputs explicit, then delegate to the
main implementations.
