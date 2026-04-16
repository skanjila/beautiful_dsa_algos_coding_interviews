# Hashing Deep Dive

This directory is for problems where constant-time lookup is the primary
pattern. `two_sum` belongs here because the standard unsorted-array interview
solution is a hash map, not a two-pointer scan.

## Interview Approach

When you hear:

- "find two values that add to a target"
- "need a linear-time solution"
- "input is not guaranteed to be sorted"

your first pattern check should be a hash map.

Stay calm by saying the invariant out loud:

- the map stores values I have already seen
- for the current value, I only need to know whether its complement was seen earlier

That naturally leads to a one-pass solution.

## `two_sum`

Returns the indices of two elements whose values sum to the target.

### Why hashing is the right pattern

The brute-force solution checks every pair in `O(N^2)`. The key observation is
that for each value `x`, the only thing that matters is whether `target - x`
has already appeared. A hash map answers that lookup in expected `O(1)` time.

### Core algorithm

1. Walk through the array once.
2. For each value, compute the complement `target - value`.
3. If the complement is already in the map, return the saved index and the current index.
4. Otherwise store the current value and index in the map.

### Big O

- time: `O(N)` because each number is processed once, and each hash-map lookup
  for the needed complement is expected constant time.
- space: `O(N)` because in the worst case you store every previously seen value
  in the map before finding the answer.

## `edge_cases`

The wrapper makes `None` inputs and arrays shorter than two elements explicit.
For valid inputs it preserves the same `O(N)` behavior as the main function.

## `contains_duplicate`

Checks whether any value repeats.

- Insert values into a set as you scan.
- The first repeat ends the search.
- Interview approach: one of the cleanest "seen set" problems in interviews.
- Big O: `O(N)` time and `O(N)` space in the worst case.

## `valid_anagram`

Checks whether two strings contain the same character counts.

- Count one string and cancel with the other.
- Interview approach: when order does not matter but multiplicity does, think
  frequency map immediately.
- Big O: `O(N)` time, `O(U)` space for distinct characters.

## `group_anagrams`

Buckets words by a canonical anagram signature.

- Sort each word or build a frequency signature.
- Interview approach: normalize each word into a key, then group by that key.
- Big O: `O(N * K log K)` with sorted-string signatures.
