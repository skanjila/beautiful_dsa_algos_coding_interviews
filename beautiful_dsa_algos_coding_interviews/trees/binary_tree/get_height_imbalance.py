from typing import Tuple

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def get_height_imbalance(root: TreeNode) -> Tuple[int, bool]:
    """
    Return ``(height, balanced)`` for the tree rooted at ``root``.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    if root is None:
        return 0, True

    left_height, left_balanced = get_height_imbalance(root.left)
    right_height, right_balanced = get_height_imbalance(root.right)
    balanced = (
        left_balanced
        and right_balanced
        and abs(left_height - right_height) <= 1
    )
    return max(left_height, right_height) + 1, balanced
