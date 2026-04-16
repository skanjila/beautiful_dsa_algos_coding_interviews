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
- Big O for the current implementation: `O(M^2 * N)` time and `O(N)` space.
  Read that as: for each discovered word, the algorithm tries changing many
  character positions, and building those candidate words costs work
  proportional to the word length. The queue and visited structures grow with
  the number of words.

## `dfs`

Contains the grid and graph DFS problems under `search/dfs`.

- Use this section when the question is about exhaustive exploration,
  component marking, reverse reachability, or graph cloning.
- Good starting problems: `number_of_islands`, `max_area_of_island`,
  `clone_graph`, `pacific_atlantic_water_flow`, `surrounded_regions`.

See [search/dfs/DEEP_DIVE.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/beautiful_dsa_algos_coding_interviews/search/dfs/DEEP_DIVE.md)
for the detailed breakdown.
