from typing import List, Optional

from .tree_node import TreeNode


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    Return the kth smallest value in a BST using iterative inorder traversal.

    Time complexity: O(H + K) in the common analysis because the traversal first
    walks down height H and then visits nodes in sorted order until the kth one.
    Space complexity: O(H) for the explicit stack.
    """
    if root is None or k <= 0:
        raise ValueError("root must be non-null and k must be positive")

    stack: List[TreeNode] = []
    current = root
    visited = 0

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        visited += 1
        if visited == k:
            return current.val
        current = current.right

    raise ValueError("k is larger than the number of nodes in the BST")
