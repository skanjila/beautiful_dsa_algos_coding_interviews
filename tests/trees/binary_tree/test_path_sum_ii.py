from beautiful_dsa_algos_coding_interviews.trees.binary_tree.path_sum_ii import path_sum
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def test_path_sum_ii_returns_all_matching_paths():
    root = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
    )
    assert path_sum(root, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]


def test_path_sum_ii_empty_tree():
    assert path_sum(None, 0) == []
