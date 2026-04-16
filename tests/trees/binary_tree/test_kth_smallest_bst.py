import pytest

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.kth_smallest_bst import kth_smallest
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def test_kth_smallest_bst_returns_sorted_position():
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert kth_smallest(root, 3) == 3


def test_kth_smallest_bst_invalid_k():
    with pytest.raises(ValueError):
        kth_smallest(TreeNode(1), 2)
