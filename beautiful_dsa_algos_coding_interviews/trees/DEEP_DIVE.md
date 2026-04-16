# Trees Deep Dive

The concrete implementations currently live under `binary_tree/`.

## Interview Approach

For tree questions, ask what information flows upward or downward:

- children to parent -> postorder DFS
- parent to children with bounds/path state -> preorder DFS
- level-by-level output -> BFS

This one decision usually cuts the solution space down immediately.

Tree problems usually rely on one of these patterns:

- postorder DFS when information flows upward from children
- preorder or BFS when information flows level by level
- recursion with bounds or path state when correctness depends on ancestors

See `binary_tree/DEEP_DIVE.md` for the function-by-function breakdown.
