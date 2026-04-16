from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def invert_binary_tree_recursive(root: TreeNode) -> TreeNode:
    """
    Recursively swap every node's children in place.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    if root is None:
        return None

    root.left, root.right = (
        invert_binary_tree_recursive(root.right),
        invert_binary_tree_recursive(root.left),
    )
    return root
