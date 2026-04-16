# Dynamic Programming Deep Dive

Dynamic programming is about solving overlapping subproblems once and reusing
their answers.

## Interview Approach

Under pressure, force yourself to answer these questions in order:

1. What subproblem does `dp[i]` or `dp[state]` represent?
2. What recurrence connects a state to smaller states?
3. What are the base cases?
4. Do I want top-down memoization or bottom-up tabulation?

If you can define the state clearly, the rest of the solution usually follows.

## `coin_change`

Finds the minimum number of coins needed to make a target amount.

- State: `dp[x]` is the fewest coins needed for amount `x`.
- Transition: try every coin and take `min(dp[x - coin] + 1)`.
- Pattern to use quickly: unbounded knapsack / minimum-cost DP.
- Big O: `O(amount * len(coins))` time because for every target amount from
  `1` to `amount`, the code tries every coin once. Space is `O(amount)` because
  the DP table stores one best answer for each intermediate amount.

## `word_break`

Checks whether a string can be segmented into dictionary words.

- State: `dp[i]` means the prefix `s[:i]` is segmentable.
- Transition: if some earlier prefix is valid and the substring from that
  prefix to `i` is a dictionary word, then `dp[i] = True`.
- Pattern to use quickly: prefix segmentation DP.
- Big O: `O(N^2)` time in the common analysis because each starting index may
  scan forward across many possible ending indices when checking substrings.
  Space is `O(N)` because the boolean DP array stores one reachable-state flag
  per string index.
