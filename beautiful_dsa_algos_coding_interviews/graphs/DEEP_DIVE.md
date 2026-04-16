# Graphs Deep Dive

These problems use traversal, topological sorting, shortest paths, coloring, or
memoized search on graph-like state spaces.

## Interview Approach

First translate the problem into graph language:

- what are the nodes?
- what are the edges?
- is the graph directed or undirected?
- do I need traversal, shortest path, or cycle detection?

Fast pattern map:

- need shortest steps with uniform cost -> BFS
- need reachability or components -> DFS/BFS
- need to order dependencies -> topological sort
- need weighted shortest path with non-negative edges -> Dijkstra
- need to test two-group compatibility -> BFS/DFS coloring
- need to validate an undirected tree -> edge count + connectivity
- need repeated subproblem counting on a grid -> DFS + memoization or DP

## `can_finish`

Kahn's algorithm for topological sorting.

- Build indegrees and adjacency lists.
- Repeatedly remove zero-indegree nodes.
- If all nodes are processed, the course graph is acyclic.
- Pattern to use quickly: topological sort with indegree counting.
- Big O: `O(V + E)` time because building the adjacency list touches each edge
  once and the topological traversal processes each vertex and edge once more.
  Space is `O(V + E)` for the adjacency list plus indegree bookkeeping.

## `can_finish_dfs`

Depth-first cycle detection for the same course-schedule problem.

- Tracks the active recursion stack to detect back-edges.
- Clears resolved prerequisite lists to memoize safe subgraphs.
- Pattern to use quickly: DFS cycle detection with visiting/visited state.
- Big O: `O(V + E)` time because DFS marks each course once and walks each
  prerequisite edge once before memoizing the result. Space is `O(V + E)` for
  the graph plus recursion/visited state.

## `find_course_order`

Topological sort that returns an actual valid ordering.

- Same indegree pattern as `can_finish`, but preserves the output sequence.
- Pattern to use quickly: dependency ordering, not only cycle detection.
- Big O: `O(V + E)` because it is the same Kahn traversal with one output list.

## `connected_components`

Counts connected components in an adjacency matrix.

- Start DFS whenever you encounter an unvisited node.
- Each fresh DFS marks one full component.
- Pattern to use quickly: connected-component traversal.
- Big O: `O(N^2)` time because in an adjacency matrix representation, exploring
  one node means scanning an entire row of length `N`, and that can happen for
  up to `N` nodes. Space is `O(N)` for the visited structure and DFS stack.

## `valid_tree`

Checks whether an undirected graph is exactly one connected acyclic tree.

- First use the invariant that a tree with `n` nodes must have `n - 1` edges.
- Then run one traversal to verify connectivity.
- Pattern to use quickly: structural graph validation.
- Big O: `O(V + E)` because edge counting is constant-time metadata and DFS is linear.

## `is_bipartite`

Uses BFS coloring to check whether neighboring nodes can always take opposite colors.

- Good pattern for "can these constraints be split into two compatible groups?"
- Pattern to use quickly: graph coloring / parity constraints.
- Big O: `O(V + E)` because every node is colored once and each edge is checked across adjacency lists.

## `network_delay_time`

Dijkstra's algorithm for weighted shortest paths with non-negative edges.

- Use a min-heap of current best-known arrival times.
- Finalize a node the first time it is popped from the heap.
- Pattern to use quickly: weighted shortest path.
- Big O: `O((V + E) log V)` because heap operations are logarithmic in the active frontier size.

## `unique_paths`

Counts paths through an obstacle grid using DFS plus memoization.

- Recursive choice: move right or move down.
- Memoization turns overlapping subproblems into linear work over grid cells.
- Pattern to use quickly: DFS with memoization on a grid.
- Big O: `O(R * C)` time because each grid cell is solved once and memoized.
  Space is `O(R * C)` because the memo table stores one count per cell.

## `edge_cases`

The wrappers add explicit guards for empty graphs, empty prerequisite lists, and
empty grids. They preserve the wrapped algorithm’s asymptotic complexity for
non-trivial inputs.
