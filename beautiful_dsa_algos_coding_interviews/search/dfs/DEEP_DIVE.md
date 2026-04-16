# DFS Deep Dive

Depth-first search is the default pattern when you need to fully explore one
path before backing up.

## Interview Approach

Start by naming the DFS shape:

- grid flood fill
- graph traversal with visited set
- recursive state expansion
- boundary-reachable marking

Under pressure, say these out loud:

1. what is one node or cell?
2. what are its neighbors?
3. how do I mark something as visited?
4. when do I stop the recursion?

If you define those four pieces clearly, the code usually becomes mechanical.

## `number_of_islands`

Counts connected land components in a grid.

- Pattern: flood fill on a grid.
- Recognition cue: "count connected regions in a binary matrix".
- Big O: `O(R * C)` time because each land cell is marked once and never
  revisited by DFS. Space is `O(R * C)` in the worst case when one large island
  makes the recursion stack as deep as the number of cells.

## `max_area_of_island`

Finds the largest connected land area.

- Pattern: DFS area accumulation.
- Recognition cue: "compute size of each connected component".
- Big O: `O(R * C)` time because each cell can contribute to area counting only
  once after it is marked visited. Space is `O(R * C)` in the worst case from a
  single deep recursive component.

## `clone_graph`

Creates a deep copy of a graph.

- Pattern: DFS with a visited/cloned map.
- Recognition cue: "copy graph with cycles".
- Big O: `O(V + E)` time because each original node is cloned once and each
  edge is followed once while populating neighbor lists. Space is `O(V)` for the
  clone map and recursion stack, not counting the cloned graph itself.

## `pacific_atlantic_water_flow`

Finds cells that can reach two boundaries.

- Pattern: reverse-reachability DFS from the boundaries inward.
- Recognition cue: "can reach both sides" often means run traversals from the
  destinations backward instead of from each source forward.
- Big O: `O(R * C)` time because each cell is inserted into the Pacific and/or
  Atlantic reachable sets at most once per ocean traversal. Space is `O(R * C)`
  because those reachable sets can each grow to the full grid.

## `surrounded_regions`

Captures only regions not connected to the border.

- Pattern: mark safe border-connected regions first, then flip the rest.
- Recognition cue: when the question is phrased as "capture surrounded cells",
  start from the border because border-connected cells can never be captured.
- Big O: `O(R * C)` time because the border-marking DFS and the final flip pass
  together still touch each cell only a constant number of times. Space is
  `O(R * C)` in the worst case from recursion over a large connected region.

## Calm Interview Pattern Map

- count components -> DFS/BFS flood fill
- measure component size -> DFS with accumulated return value
- copy graph -> DFS + visited map
- preserve border-connected cells -> DFS from boundaries
- determine dual reachability -> DFS from both destination sets
