# Binary Tree Deep Dive

Before reading the complexity notes in this file:

- `N` = number of nodes
- `H` = tree height
- `W` = maximum width of any level

That makes the space terms easier to read:

- `O(H)` usually means recursion stack or explicit stack along one root-to-leaf path
- `O(W)` usually means queue size during BFS

## Structural helpers

- `tree_node.TreeNode`: generic node class, `O(1)` construction
- `invert_binary_tree_iterative.TreeNode`: local node class used by that file

## Interview Approach

Start by classifying the tree problem:

- need height, diameter, balance, or path combination -> postorder DFS
- need level view or width -> BFS
- need ancestor or validation with ancestor constraints -> DFS with returned
  subtree info or bounds

In a stressful interview, say the traversal choice before coding. That shows
control and reduces the chance of wandering into the wrong pattern.

## Depth and height

- `max_depth_postorder`: postorder DFS, `O(N)` time, `O(H)` space
- `get_height_imbalance`: returns height plus balance status, `O(N)` / `O(H)`
- `is_balanced_with_depth`: delegates to height/imbalance analysis, `O(N)` / `O(H)`

Pattern to use quickly: postorder DFS because each answer depends on child answers.

## Traversal fundamentals

- `inorder_traversal_iterative`: explicit stack inorder traversal for sorted BST output or general inorder traversal, `O(N)` / `O(H)`
- `binary_tree_level_order`: standard BFS by levels, `O(N)` / `O(W)`
- `binary_tree_zigzag_level_order`: level-order traversal with alternating direction, `O(N)` / `O(W)`

Pattern to use quickly:

- need sorted order from a BST -> inorder
- need nodes grouped per level -> BFS
- need alternating left/right level view -> BFS with per-level reversal logic

## Shape transforms

- `invert_binary_tree_iterative`: explicit stack inversion, `O(N)` / `O(H..N)`
- `invert_binary_tree_recursive`: recursive inversion, `O(N)` / `O(H)`

Pattern to use quickly: DFS traversal that swaps children at every node.

## Path and ancestor problems

- `calc_diameter_with_depth`: longest path through any node, `O(N)` / `O(H)`
- `longest_univalue_path`: longest same-value path, `O(N)` / `O(H)`
- `lowest_common_ancestor`: one DFS that returns ancestor candidates upward, `O(N)` / `O(H)`
- `tree_paths`: enumerate root-to-leaf paths, `O(N * L)` / `O(H)`
- `path_sum_ii`: root-to-leaf path accumulation with backtracking, `O(N * H)` / `O(H)`

Pattern to use quickly:

- combine left/right path contributions -> postorder DFS
- return one node upward as an answer candidate -> recursive ancestor search
- accumulate root-to-leaf state -> DFS with path list

## Validation and views

- `validate_binary_tree.is_valid_bst`: DFS with numeric bounds, `O(N)` / `O(H)`
- `kth_smallest_bst`: iterative inorder because BST inorder is sorted, `O(H + K)` / `O(H)`
- `right_side_view`: BFS by levels, `O(N)` / `O(W)`
- `rightmost_node_binary_tree`: same right-side-view pattern, `O(N)` / `O(W)`
- `vertical_order_traversal.vertical_order_bfs`: BFS plus column index, `O(N)` / `O(N)`
- `widest_binary_tree_level`: BFS with positional indices, `O(N)` / `O(W)`

Pattern to use quickly:

- BST validity -> pass lower/upper bounds downward
- kth-smallest in BST -> inorder traversal because it visits nodes in sorted order
- anything that says "per level", "side view", or "width" -> BFS

## Serialization and representation

- `serialize_deserialize_binary_tree.Codec`: level-order serialization that preserves null structure, `O(N)` time and space for both directions

Pattern to use quickly:

- if the interviewer wants a tree encoded and rebuilt later, you must preserve
  null children as well as values, otherwise different shapes collapse into the
  same token sequence

## Edge-case wrappers

`edge_cases.py` contains explicit guards for:

- empty trees
- missing target nodes
- empty result defaults

These wrappers do not change the asymptotic cost of the main algorithms.
