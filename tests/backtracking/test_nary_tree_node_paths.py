import pytest
from beautiful_dsa_algos_coding_interviews.backtracking.n_ary_tree_node import NAryTreeNode
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_paths import treePaths


def build_sample_tree():
    """
    Builds this N-ary tree:
            1
          / | \
         2  3  4
           / \
          5   6
    Expected root-to-leaf paths:
      ["1->2", "1->3->5", "1->3->6", "1->4"]
    """
    node5 = NAryTreeNode(5)
    node6 = NAryTreeNode(6)
    node3 = NAryTreeNode(3, [node5, node6])
    node2 = NAryTreeNode(2)
    node4 = NAryTreeNode(4)
    root = NAryTreeNode(1, [node2, node3, node4])
    return root


def test_empty_tree():
    assert treePaths(None, None) == []


def test_single_node_tree():
    root = NAryTreeNode(10)
    assert treePaths(None, root) == ["10"]


def test_balanced_n_ary_tree():
    root = build_sample_tree()
    paths = treePaths(None, root)
    expected = ["1->2", "1->3->5", "1->3->6", "1->4"]
    assert sorted(paths) == sorted(expected)


def test_unbalanced_tree():
    """
    Tree:
         1
          \
           2
            \
             3
    Expected path: ["1->2->3"]
    """
    node3 = NAryTreeNode(3)
    node2 = NAryTreeNode(2, [node3])
    root = NAryTreeNode(1, [None, node2])
    assert treePaths(None, root) == ["1->2->3"]


def test_multiple_leaf_nodes():
    """
    Tree:
            10
          /  |  \
        20  30  40
           / \
         50  60
    Expected: ["10->20", "10->30->50", "10->30->60", "10->40"]
    """
    node50 = NAryTreeNode(50)
    node60 = NAryTreeNode(60)
    node30 = NAryTreeNode(30, [node50, node60])
    node20 = NAryTreeNode(20)
    node40 = NAryTreeNode(40)
    root = NAryTreeNode(10, [node20, node30, node40])
    result = treePaths(None, root)
    expected = ["10->20", "10->30->50", "10->30->60", "10->40"]
    assert sorted(result) == sorted(expected)
