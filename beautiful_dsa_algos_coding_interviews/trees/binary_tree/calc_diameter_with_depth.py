from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def calc_diameter_with_depth(root: TreeNode) -> int:
    """
    Return the diameter measured in edges.

    Time complexity: O(N)
    Space complexity: O(H) recursion depth, where H is the tree height.
    """

    best = 0

    def depth(node: TreeNode) -> int:
        """Return subtree depth while updating the best diameter.

        Time complexity: O(size of subtree)
        Space complexity: O(H) recursion depth.
        """
        nonlocal best
        if node is None:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        best = max(best, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    depth(root)
    return best


def diameter_of_binary_tree(root: TreeNode) -> int:
    """Alias for ``calc_diameter_with_depth``.

    Time complexity: O(N)
    Space complexity: O(H)
    """
    return calc_diameter_with_depth(root)
