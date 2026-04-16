# Trees Deep Dive

The concrete implementations currently live under `binary_tree/`.

## Why Trees Matter In Interviews

Tree problems are one of the densest interview categories because they test:

- recursion control
- traversal choice
- state management across levels or root-to-leaf paths
- the ability to derive an answer from child subproblems

That is exactly why Alex Xu and Shaun Gunawardane's interview-pattern framing is
useful here: most tree problems collapse once you identify whether the answer
flows upward, downward, or level by level.

## Interview Approach

For tree questions, ask what information flows upward or downward:

- children to parent -> postorder DFS
- parent to children with bounds/path state -> preorder DFS
- level-by-level output -> BFS

This one decision usually cuts the solution space down immediately.

Tree problems usually rely on one of these patterns:

- postorder DFS when information flows upward from children
- preorder DFS when ancestors constrain descendants
- path DFS when the current root-to-node state matters
- BFS when the question is phrased per level, side, or width
- inorder traversal when BST ordering matters
- serialization traversal when structure must be preserved across null children

## Coverage Map

The repo now covers a broader interview-style tree set:

- traversal fundamentals: inorder, level order, zigzag level order
- structure transforms: invert tree
- height and balance: max depth, balance checks
- ancestor and path aggregation: LCA, diameter, univalue path, root-to-leaf paths, path sum
- BST reasoning: validation and kth-smallest
- view problems: right side view, vertical order, widest level
- representation problems: serialize / deserialize

See `binary_tree/DEEP_DIVE.md` for the function-by-function breakdown.
