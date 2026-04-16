# Strings Deep Dive

String questions usually break into a few repeatable interview shapes:

- normalization and scanning
- parsing and encoding
- palindrome logic
- mapping or bijection constraints
- permutation and grouping logic

## `generate_anagrams`

Builds all unique permutations of a string.

- Sort first so duplicate letters can be skipped cleanly at the same depth.
- Use a `used` array to track the active path.
- Interview approach: recognize this as a permutation problem over characters.
- Big O: `O(N * N!)` time because there are `N!` distinct permutations and each
  completed permutation costs `O(N)` to materialize as a string. Recursion
  depth is `O(N)` because one character is chosen per level.

## `longest_palindromic_substring`

Uses expand-around-center.

- Every palindrome has a center.
- Try odd centers `(i, i)` and even centers `(i, i + 1)`.
- Expand while characters match and track the longest valid window.
- Interview approach: if the goal is longest palindromic substring, center
  expansion is usually the fastest correct answer to reach in a whiteboard setting.
- Big O: `O(N^2)` time because there are `O(N)` possible centers and each
  center expansion may walk outward across many characters. Auxiliary space is
  `O(1)` because the expansion uses pointers instead of a DP table.

### Helper functions

- `is_palindrome`: direct palindrome check using reverse comparison
- `brute_force_longest_pal_len`: validation helper with cubic worst-case time

## `longest_common_prefix`

Finds the shared prefix across many strings.

- Keep a candidate prefix and shrink it until every string matches.
- Interview approach: when the answer must be common across all strings, keep a
  monotonic candidate and shorten it on mismatch.
- Big O: `O(S)` where `S` is the total number of compared characters.

## `encode_decode_strings`

Turns a list of strings into one reversible transport string and back.

- Prefix each string with its length.
- Interview approach: when delimiters may appear inside payloads, use explicit
  lengths instead of delimiter-only splitting.
- Big O: `O(total_chars)` for both directions.

## `string_to_integer_atoi`

Parses signed integers from messy input.

- Skip spaces, parse sign, then consume the numeric run.
- Interview approach: this is a parser-state problem with bounds checking.
- Big O: `O(N)` time, `O(1)` space.

## `isomorphic_strings`

Checks whether one string can map one-to-one onto another.

- Maintain both forward and reverse maps.
- Interview approach: whenever a mapping must be one-to-one, use two hash maps
  so collisions are caught from both directions.
- Big O: `O(N)` time, `O(U)` space for distinct characters.

## `edge_cases`

Wrappers make null handling explicit, then defer to the main string algorithms.
