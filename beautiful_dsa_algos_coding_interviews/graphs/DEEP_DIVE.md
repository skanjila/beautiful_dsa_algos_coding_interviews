# Graphs Deep Dive

These problems use graph traversal, topological sorting, or memoized search.

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
- need repeated subproblem counting on a grid -> DFS + memoization or DP

## `can_finish`

Kahn's algorithm for topological sorting.

- Build indegrees and adjacency lists.
- Repeatedly remove zero-indegree nodes.
- If all nodes are processed, the course graph is acyclic.
- Pattern to use quickly: topological sort with indegree counting.
- Big O: `O(V + E)` time, `O(V + E)` space.

## `can_finish_dfs`

Depth-first cycle detection for the same course-schedule problem.

- Tracks the active recursion stack to detect back-edges.
- Clears resolved prerequisite lists to memoize safe subgraphs.
- Pattern to use quickly: DFS cycle detection with visiting/visited state.
- Big O: `O(V + E)` time, `O(V + E)` space.

## `connected_components`

Counts connected components in an adjacency matrix.

- Start DFS whenever you encounter an unvisited node.
- Each fresh DFS marks one full component.
- Pattern to use quickly: connected-component traversal.
- Big O: `O(N^2)` time because matrix rows are scanned, `O(N)` space.

## `unique_paths`

Counts paths through an obstacle grid using DFS plus memoization.

- Recursive choice: move right or move down.
- Memoization turns overlapping subproblems into linear work over grid cells.
- Pattern to use quickly: DFS with memoization on a grid.
- Big O: `O(R * C)` time, `O(R * C)` space.

## `edge_cases`

The wrappers add explicit guards for empty graphs, empty prerequisite lists, and
empty grids. They preserve the wrapped algorithm’s asymptotic complexity for
non-trivial inputs.
