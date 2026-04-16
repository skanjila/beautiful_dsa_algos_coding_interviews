# Backtracking Deep Dive

This directory covers recursive search over decision trees. The common shape is:

1. choose a candidate state
2. recurse on the smaller remaining problem
3. undo the choice before trying the next branch

## Interview Approach

Under pressure, ask three questions first:

1. What is the decision at each step?
2. What state must be carried in the recursion path?
3. What invalid partial states can be pruned early?

The fastest calm pattern is:

- define the path
- define the stopping condition
- define the branching choices
- define the undo step

If the interviewer says "all combinations", "all partitions", "all placements",
or "generate every valid arrangement", backtracking should be one of your first
pattern checks.

## `combination_sum`

Finds combinations that add to a target when candidates may be reused.

- Core idea: sort candidates, then keep recursing from the same index so the
  same value can be chosen again.
- Why it works: the recursion path is the partial combination; the remaining
  target is the unfinished work.
- Interview pattern: combination generation with pruning by sorted order and
  remaining target.
- Fast recognition cue: "find all combinations that add to a target".
- Big O: exponential search tree. In plain English, the algorithm keeps trying
  many candidate values at many recursion levels until the remaining target is
  driven to zero or below. The exact formula is less important than the shape:
  branching choices grow quickly, and the recursion depth is bounded by how
  many times the smallest candidate can fit into the target.

## `combination_sum_ii`

Finds unique combinations when each candidate can be used at most once.

- Core idea: recurse with `index + 1` after a choice so each element is consumed
  at most once.
- Duplicate control: skip equal values at the same tree depth.
- Interview pattern: subset-style backtracking with duplicate skipping.
- Fast recognition cue: "each number can be used once" plus possible duplicates.
- Big O: think "subset tree". Each element is effectively a choose-or-skip
  decision, so the search can grow toward `2^N` branches in the worst case.
  Recursion depth is `O(N)` because the path can include at most all elements.

## `generate_parentheses`

Generates all valid parentheses strings of length `2n`.

- Core idea: only add `(` if you still have opens left, and only add `)` if the
  current prefix remains valid.
- Why it matters: this is the canonical "constrained construction" interview
  problem.
- Interview pattern: build-valid-string DFS with invariant tracking.
- Fast recognition cue: "generate all valid strings" where invalid prefixes can
  be ruled out immediately.
- Big O: the number of valid outputs is the main driver here. There are
  Catalan-many valid strings, and each finished string has length `2n`, so the
  work is roughly "number of valid strings times string length". Recursion
  depth is `O(n)` because you place one parenthesis at a time.

## `letter_combinations_of_phone_number`

Builds the Cartesian product of letters mapped from digits.

- Core idea: one recursion level per digit, one branch per mapped character.
- This is simpler than most backtracking tasks because there is no pruning.
- Interview pattern: Cartesian-product DFS.
- Fast recognition cue: independent choices at each position, no conflicts
  between choices.
- Big O: one recursion level per digit, with about 3 or 4 branches per level
  depending on the keypad mapping. That means the total number of outputs grows
  like "branching factor to the number of digits". Stack depth is linear in the
  number of digits.

## `n_ary_tree_node`

Lightweight node class used by tree-path examples.

- Construction is constant time aside from copying the child references.
- Big O: `O(1)` build cost, `O(k)` storage for `k` children.

## `n_queens`

Places queens row by row while preventing column and diagonal conflicts.

- Core idea: keep three constraint sets for used columns, downward diagonals,
  and upward diagonals.
- Why it works: if a placement is safe locally against those sets, it preserves
  global correctness for the partial board.
- Interview pattern: placement backtracking with constraint sets.
- Fast recognition cue: "place items on a board without conflicts".
- Big O: the search explores permutations, so the number of full arrangements
  grows factorially. Recursion depth is `O(N)` because one queen is placed per
  row.

## `palindrome_partitioning`

Splits a string into substrings such that every substring is a palindrome.

- Core idea: choose a cut only when the current prefix is a palindrome.
- This is a partitioning-style backtracking problem rather than a permutation
  or combination problem.
- Interview pattern: cut-the-string recursion.
- Fast recognition cue: "split into all valid pieces" or "partition into valid substrings".
- Big O: there can be exponentially many valid cut patterns, and each completed
  partition may need up to linear work to copy or describe its substrings.
  Recursion depth is `O(N)` because cuts move left to right through the string.

## `permutations`

Enumerates every ordering of the input list.

- Core idea: track which indices are already used in the current path.
- Interview pattern: ordering/backtracking with used flags.
- Fast recognition cue: "all orderings" or "all permutations".
- Big O: `O(N * N!)` because there are `N!` permutations and copying a full path
  costs `O(N)`.

## `subsets`

Generates the power set with duplicate skipping.

- Core idea: at each position, either include an element or move past it.
- Duplicate handling: after sorting, skip equal values at the same recursion depth.
- Interview pattern: include/exclude or subset-tree enumeration.
- Fast recognition cue: "all subsets", "power set", or "choose any number of elements".
- Big O: the power set has `2^N` subsets, and copying each finished subset can
  cost up to `O(N)`. Recursion depth is `O(N)` because the decision path can
  include every element once.

## `word_search`

Searches a board for a path spelling a word.

- Core idea: DFS from every starting cell and mark the current cell as visited
  during the active path.
- Key interview point: restore the board state after the recursive calls.
- Interview pattern: grid DFS with visited restoration.
- Fast recognition cue: "move up/down/left/right and cannot reuse the same cell".
- Big O: you may try starting DFS from many cells, and from each step the word
  search can branch in up to four directions before dead ends are ruled out.
  Recursion depth is `O(L)` because the active path cannot exceed the word
  length.

## `edge_cases`

These wrappers make boundary handling explicit:

- null or empty inputs
- negative targets
- invalid digit strings
- impossible board sizes

They do not change the underlying algorithmic shape. They mainly add constant
time guards before delegating to the main implementation.
