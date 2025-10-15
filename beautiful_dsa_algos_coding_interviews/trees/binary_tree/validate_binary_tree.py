import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Checks if a binary tree is a valid Binary Search Tree (BST).
    A valid BST must satisfy:
        - Every node's left subtree contains only values less than the node's value.
        - Every node's right subtree contains only values greater than the node's value.
        - No duplicates are allowed.

    Approach:
        We use DFS (depth-first search) with a valid range for each node:
            - Each node's value must lie strictly between a lower (min) and upper (max) bound.
            - As we go left, the upper bound becomes the current node’s value.
            - As we go right, the lower bound becomes the current node’s value.
    """

    def dfs(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        # Base case: empty subtree is always valid
        if node is None:
            return True

        # The current node must fall strictly between the allowed bounds
        if not (min_val < node.val < max_val):
            return False

        # Recursively check:
        # Left subtree: everything must be < current node's value
        # Right subtree: everything must be > current node's value
        return (
            dfs(node.left, min_val, node.val) and
            dfs(node.right, node.val, max_val)
        )

    # Start with the widest possible range
    return dfs(root, -math.inf, math.inf)
