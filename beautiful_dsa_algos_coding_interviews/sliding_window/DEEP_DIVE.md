# Sliding Window Deep Dive

Sliding window problems maintain a contiguous range while enforcing an invariant.

## Interview Approach

Ask:

- what makes the current window valid?
- what condition forces the left pointer to move?
- am I maximizing or minimizing window size?

The calm template is:

- expand right
- update window state
- while invalid, shrink left
- update answer

## `length_of_longest_substring`

Returns the longest substring without repeated characters.

- Keep `start` as the left boundary of the valid window.
- Use `last_seen` to jump `start` forward when a repeated character appears.
- Pattern to use quickly: variable-size window with last-seen map.
- Big O: `O(N)` time because the right pointer moves forward `N` times and the
  left pointer also only moves forward, never backward, so the total pointer
  movement is linear rather than quadratic. Space is `O(min(N, alphabet_size))`
  because the window map stores at most one entry per distinct character in the
  current window.

## `longest_ones`

Finds the longest binary subarray containing at most `k` zeros.

- Expand the right boundary greedily.
- Shrink from the left whenever zero count exceeds `k`.
- Pattern to use quickly: variable-size window with constraint counter.
- Big O: `O(N)` time because each array element enters the window once and
  leaves the window at most once as the left pointer advances. Space is `O(1)`
  because the algorithm tracks only counters and indices.

## `edge_cases`

Wrappers make empty inputs and invalid `k` values explicit while preserving the
underlying `O(N)` logic.
