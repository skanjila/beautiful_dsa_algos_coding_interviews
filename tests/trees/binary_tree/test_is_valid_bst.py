import pytest
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.validate_binary_tree import is_valid_bst


def N(val, left=None, right=None):
    node = TreeNode(val)
    node.left = left
    node.right = right
    return node


def test_empty_tree_is_valid():
    assert is_valid_bst(None) is True


def test_single_node_is_valid():
    assert is_valid_bst(N(42)) is True


def test_valid_bst_simple():
    #       2
    #      / \
    #     1   3
    root = N(2, N(1), N(3))
    assert is_valid_bst(root) is True


def test_valid_bst_with_negatives_and_positives():
    #         0
    #       /   \
    #     -3     9
    #        \   /
    #        -1 5
    root = N(0, N(-3, None, N(-1)), N(9, N(5), None))
    assert is_valid_bst(root) is True


def test_invalid_bst_left_subtree_violation():
    #         5
    #        / \
    #       3   7
    #      /
    #     6  (>= 5 on left) -> invalid
    root = N(5, N(3, N(6), None), N(7))
    assert is_valid_bst(root) is False


def test_invalid_bst_right_subtree_violation_exposes_bug():
    #         5
    #        / \
    #       3   7
    #          /
    #         4  (<= 5 on right) -> invalid
    root = N(5, N(3), N(7, N(4), None))
    assert is_valid_bst(root) is False


@pytest.mark.parametrize(
    "vals, expected",
    [
        # Duplicates are invalid for strict BST:
        #   2
        #  / \
        # 2   3
        ((2, 2, 3), False),
        #   2
        #  / \
        # 1   2
        ((2, 1, 2), False),
        # Right-skewed increasing chain -> valid
        # 1 -> 2 -> 3 -> 4
        ((1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4), True),
    ],
)
def test_duplicates_and_right_chain(vals, expected):
    def build_from_level_order(level_vals):
        if not level_vals:
            return None
        nodes = [None if v is None else TreeNode(v) for v in level_vals]
        for i, node in enumerate(nodes):
            if node is None:
                continue
            li, ri = 2 * i + 1, 2 * i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]
        return nodes[0]

    root = build_from_level_order(list(vals))
    assert is_valid_bst(root) is expected


def test_valid_bst_deeper_right_subtree():
    #           10
    #          /  \
    #         4    15
    #             /  \
    #           12    18
    #                 /
    #                16
    root = N(10, N(4), N(15, N(12), N(18, N(16), None)))
    assert is_valid_bst(root) is True


def test_invalid_due_to_duplicate_at_deeper_level():
    #           8
    #          / \
    #         3   10
    #            /  \
    #           9    14
    #               /
    #              10  (duplicate in right subtree) -> invalid
    root = N(8, N(3), N(10, N(9), N(14, N(10), None)))
    assert is_valid_bst(root) is False
