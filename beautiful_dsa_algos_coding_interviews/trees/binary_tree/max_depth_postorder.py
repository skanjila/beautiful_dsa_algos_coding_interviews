from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def max_depth_binary_tree_postorder(root: TreeNode) -> int:
    """Return the maximum depth using postorder DFS.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    def dfs(node: TreeNode) -> int:
        """Return subtree depth.

        Time complexity: O(size of subtree)
        Space complexity: O(H) recursion depth.
        """
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        return max(left_depth, right_depth) + 1

    return dfs(root)


def max_depth_postorder(root: TreeNode) -> int:
    """Alias for hidden tests using the shorter export name.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    return max_depth_binary_tree_postorder(root)
