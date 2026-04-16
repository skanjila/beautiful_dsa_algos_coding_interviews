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

- amortized near-constant time, often written `O(alpha(N))`, because path
  compression flattens trees during finds and union by rank/size prevents tall
  trees from forming in the first place.
- space: `O(N)` because parent and rank/size arrays store one entry per node.

Plain-English way to read that:

- treat `alpha(N)` as "so small it behaves like a constant in interviews"
- the important intuition is not the formula itself
- the important intuition is that repeated finds keep making future finds cheaper

## `count_components`

Counts connected components by starting from `n` isolated nodes and decrementing
the count whenever a successful union merges two previously separate groups.

- Pattern to use quickly: union edges, count merges.
- Big O: `O((N + E) * alpha(N))` time because initialization touches `N` nodes
  once and each of the `E` edges does a small constant number of amortized
  union/find operations. Space is `O(N)` for the union-find arrays.
