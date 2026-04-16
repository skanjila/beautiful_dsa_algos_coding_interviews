from beautiful_dsa_algos_coding_interviews.trees.binary_tree.inorder_traversal_iterative import inorder_traversal
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def test_inorder_traversal_iterative_bst_order():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert inorder_traversal(root) == [1, 2, 3]


def test_inorder_traversal_iterative_empty():
    assert inorder_traversal(None) == []
