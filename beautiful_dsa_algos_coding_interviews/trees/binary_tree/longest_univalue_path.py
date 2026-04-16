from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def longest_univalue_path(root: TreeNode) -> int:
    """
    Return the longest path of equal-valued nodes measured in edges.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    best = 0

    def dfs(node: TreeNode) -> int:
        """Return the longest downward same-value chain from ``node``.

        Time complexity: O(size of subtree)
        Space complexity: O(H) recursion depth.
        """
        nonlocal best
        if node is None:
            return 0

        left_length = dfs(node.left)
        right_length = dfs(node.right)

        extend_left = 0
        extend_right = 0
        if node.left and node.left.val == node.val:
            extend_left = left_length + 1
        if node.right and node.right.val == node.val:
            extend_right = right_length + 1

        best = max(best, extend_left + extend_right)
        return max(extend_left, extend_right)

    dfs(root)
    return best
