# tests/trees/test_invert_binary_tree.py
import pytest

# --- SUT types ---
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Your current (buggy) function, left here so a test can catch it.
def invert_binary_tree_iterative_buggy(root: TreeNode) -> TreeNode:
    if not root:
        return None
    stack = [root]
    while stack:
        popped_node = stack.pop()
        # BUG: no swap here
        popped_node.left, popped_node.right = popped_node.left, popped_node.right
        if popped_node.left:
            stack.append(popped_node.left)
        if popped_node.right:
            stack.append(popped_node.right)
    return root

# Corrected version (what the rest of the tests will validate).
def invert_binary_tree_iterative(root: TreeNode) -> TreeNode:
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left  # <-- swap
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


# --- Test helpers ---
def build_tree_level(values):
    """
    Build a binary tree from a level-order list with None for missing nodes.
    Example: [4,2,7,1,3,6,9] -> the classic LeetCode example.
    """
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

def to_level_list(root):
    """Serialize a tree to level-order list (trim trailing Nones for stable compares)."""
    if not root:
        return []
    out, q = [], [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    # trim trailing None
    while out and out[-1] is None:
        out.pop()
    return out

def test_empty_tree():
    assert invert_binary_tree_iterative(None) is None


def test_single_node_tree():
    root = TreeNode(42)
    same_obj = invert_binary_tree_iterative(root)
    # Structure unchanged; identity preserved
    assert same_obj is root
    assert to_level_list(root) == [42]


def test_two_levels_balanced():
    # In:  [4,2,7,1,3,6,9]
    # Out: [4,7,2,9,6,3,1]
    root = build_tree_level([4, 2, 7, 1, 3, 6, 9])
    invert_binary_tree_iterative(root)
    assert to_level_list(root) == [4, 7, 2, 9, 6, 3, 1]


def test_unbalanced_left_heavy_becomes_right_heavy():
    # In:  [1,2,None,3,None,4]  (a left chain)
    # Out: [1,None,2,None,3,None,4] (a right chain)
    root = build_tree_level([1, 2, None, 3, None, 4])
    invert_binary_tree_iterative(root)
    assert to_level_list(root) == [1, None, 2, None, 3, None, 4]


def test_already_symmetric_structure():
    # In:  [1,2,2,3,4,4,3] (mirror-symmetric)
    # After inversion it stays the same by value layout.
    root = build_tree_level([1, 2, 2, 3, 4, 4, 3])
    invert_binary_tree_iterative(root)
    assert to_level_list(root) == [1, 2, 2, 3, 4, 4, 3]


def test_in_place_mutation_and_return_value_identity():
    root = build_tree_level([1, 2, 3])
    returned = invert_binary_tree_iterative(root)
    assert returned is root, "Function should return the same root reference"
    assert to_level_list(root) == [1, 3, 2]
