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
- Big O: `O(N)` time, `O(N)` space because the cleaned string is rebuilt.

## `three_sum`

Finds unique triplets that sum to zero.

- Sort the array first.
- Fix one value and solve the remaining two-sum problem with left/right pointers.
- Skip duplicates at the fixed index and at both moving pointers.
- Pattern to use quickly: sort + fix one value + two-sum with two pointers.
- Big O: `O(N^2)` time, `O(1)` auxiliary space excluding output.

## `three_sum_bf`

Brute-force reference for the same problem.

- Try every triplet combination.
- Use a set to deduplicate sorted triplets.
- Interview value: useful as a baseline before optimizing to the two-pointer solution.
- Big O: `O(N^3)` time, `O(K)` extra space for found triplets.

## `edge_cases`

Wrappers make null handling and too-short inputs explicit, then delegate to the
main implementations.
