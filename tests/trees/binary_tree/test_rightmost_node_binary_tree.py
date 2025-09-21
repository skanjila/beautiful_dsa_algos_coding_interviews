# tests/trees/binary_tree/test_rightmost_node_binary_tree.py
import pytest

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.rightmost_node_binary_tree import \
    rightmost_node_binary_tree
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


# --- helpers ---

def build_tree_level(values):
    """
    Build a binary tree from a level-order list with None for missing nodes.
    Example: [1, 2, 3, None, 5, None, 4]
    """
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node is not None:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# --- tests ---

def test_empty_tree_returns_empty_list_or_none():
    # Prefer [] semantically, but accept None if your implementation returns that.
    result = rightmost_node_binary_tree(None)
    assert result == [] or result is None


def test_single_node_tree():
    root = TreeNode(42)
    assert rightmost_node_binary_tree(root) == [42]


def test_perfect_two_levels():
    #      1
    #     / \
    #    2   3
    root = build_tree_level([1, 2, 3])
    assert rightmost_node_binary_tree(root) == [1, 3]


def test_perfect_three_levels():
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6  7
    root = build_tree_level([1, 2, 3, 4, 5, 6, 7])
    assert rightmost_node_binary_tree(root) == [1, 3, 7]


def test_right_skewed_tree():
    # 1 -> 2 -> 3
    root = build_tree_level([1, None, 2, None, 3])
    assert rightmost_node_binary_tree(root) == [1, 2, 3]


def test_left_skewed_tree():
    # 1
    # └─2
    #   └─3
    root = build_tree_level([1, 2, None, 3])
    assert rightmost_node_binary_tree(root) == [1, 2, 3]


def test_gappy_levels_rightmost_is_left_child():
    #     1
    #    / \
    #   2   3
    #    \   \
    #     5   4
    # Right side view: [1, 3, 4]
    root = build_tree_level([1, 2, 3, None, 5, None, 4])
    assert rightmost_node_binary_tree(root) == [1, 3, 4]


def test_unbalanced_with_missing_right_subtree_low():
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # Right side view: [1, 3, 4]
    root = build_tree_level([1, 2, 3, 4])
    assert rightmost_node_binary_tree(root) == [1, 3, 4]


def test_duplicates():
    #       1
    #      / \
    #     1   1
    #    /
    #   1
    root = build_tree_level([1, 1, 1, 1])
    assert rightmost_node_binary_tree(root) == [1, 1, 1]


@pytest.mark.parametrize(
    "values,expected",
    [
        # mixed: rightmost nodes appear on alternating sides
        ([10, 5, 15, None, 7, 12, None], [10, 15, 12]),
        # deeper left subtree but right leaf present at bottom
        ([1, 2, 3, 4, None, None, None, 8, 9], [1, 3, 4, 9]),
        # zig-zag shape
        ([1, None, 2, 3, None, None, 4], [1, 2, 3, 4]),
    ],
)
def test_parametrized_rightmost_views(values, expected):
    root = build_tree_level(values)
    assert rightmost_node_binary_tree(root) == expected
