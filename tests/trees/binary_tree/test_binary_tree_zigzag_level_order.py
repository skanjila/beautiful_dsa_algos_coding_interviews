from beautiful_dsa_algos_coding_interviews.trees.binary_tree.binary_tree_zigzag_level_order import zigzag_level_order
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def test_zigzag_level_order_basic_tree():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag_level_order(root) == [[3], [20, 9], [15, 7]]


def test_zigzag_level_order_single_node():
    assert zigzag_level_order(TreeNode(1)) == [[1]]
