from beautiful_dsa_algos_coding_interviews.trees.binary_tree.binary_tree_level_order import level_order
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def test_level_order_basic_tree():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_level_order_empty_tree():
    assert level_order(None) == []
