# Search Deep Dive

The `search` package is split by traversal style.

## Interview Approach

Decide traversal style before touching code:

- shortest path with equal edge cost -> BFS
- exhaustive path exploration or recursive structure -> DFS

Naming the traversal pattern out loud buys time and reduces random coding.

## `bfs`

Contains `word_ladder`, a shortest-path problem solved with breadth-first search.

- BFS is the correct pattern when every edge has uniform cost and you need the
  shortest number of steps.
- Big O for the current implementation: `O(M^2 * N)` time, `O(N)` space.

## `dfs`

This subdirectory is currently a placeholder for future depth-first search examples.
