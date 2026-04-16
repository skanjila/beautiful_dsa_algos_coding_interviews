# Union Find Deep Dive

Union-find, also called disjoint-set union, is for tracking connected groups
under repeated merge operations.

## Interview Approach

Reach for union-find when you hear:

- dynamically connect nodes
- count connected components
- detect whether two nodes are already connected
- merge groups efficiently

The fast mental model is:

- `find(x)` tells you the representative of x's group
- `union(a, b)` merges the two groups if they were different

## `union_find`

Implements:

- path compression in `find`
- union by rank in `union`

Why that matters:

- path compression flattens trees during lookups
- union by rank prevents trees from becoming tall

Big O:

- amortized near-constant time, often written `O(alpha(N))`
- space: `O(N)`

## `count_components`

Counts connected components by starting from `n` isolated nodes and decrementing
the count whenever a successful union merges two previously separate groups.

- Pattern to use quickly: union edges, count merges.
- Big O: `O((N + E) * alpha(N))` time, `O(N)` space.
