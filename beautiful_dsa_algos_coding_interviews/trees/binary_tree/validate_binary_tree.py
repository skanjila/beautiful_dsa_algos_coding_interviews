import math
from typing import Optional
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Top-down min/max validation for a strict BST (no equal duplicates)."""
    def dfs(node: Optional[TreeNode], floor: float, ceiling: float) -> bool:
        if node is None:
            return True
        # current node must be inside (floor, ceiling)
        if not (floor < node.val < ceiling):
            return False
        # left: (floor, node.val)
        if not dfs(node.left, floor, node.val):
            return False
        # right: (node.val, ceiling)  <-- FIXED: node.val is the new floor
        if not dfs(node.right, node.val, ceiling):
            return False
        return True

    return dfs(root, -math.inf, math.inf)
