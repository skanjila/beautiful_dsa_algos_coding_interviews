from beautiful_dsa_algos_coding_interviews.trees.binary_tree.get_height_imbalance import (
    get_height_imbalance,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def is_balanced_with_depth(root: TreeNode) -> bool:
    """
    Return True when every subtree differs in height by at most one.

    Time complexity: O(N)
    Space complexity: O(H)
    """

    return get_height_imbalance(root)[1]
