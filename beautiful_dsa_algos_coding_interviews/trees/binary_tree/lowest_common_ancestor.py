from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Return the lowest common ancestor of nodes ``p`` and ``q``.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    if root is None or root is p or root is q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left or right
