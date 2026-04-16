# Strings Deep Dive

## `generate_anagrams`

Builds all unique permutations of a string.

- Sort first so duplicate letters can be skipped cleanly at the same depth.
- Use a `used` array to track the active path.
- Interview approach: recognize this as a permutation problem over characters.
- Big O: `O(N * N!)` time, `O(N)` recursion depth.

## `longest_palindromic_substring`

Uses expand-around-center.

- Every palindrome has a center.
- Try odd centers `(i, i)` and even centers `(i, i + 1)`.
- Expand while characters match and track the longest valid window.
- Interview approach: if the goal is longest palindromic substring, center
  expansion is usually the fastest correct answer to reach in a whiteboard setting.
- Big O: `O(N^2)` time, `O(1)` auxiliary space.

### Helper functions

- `is_palindrome`: direct palindrome check using reverse comparison
- `brute_force_longest_pal_len`: validation helper with cubic worst-case time

## `edge_cases`

Wrappers make null handling explicit, then defer to the main string algorithms.
