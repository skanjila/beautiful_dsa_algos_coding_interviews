from typing import List, Optional

from .tree_node import TreeNode


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Return inorder traversal using an explicit stack.

    Time complexity: O(N) because every node is pushed and popped once.
    Space complexity: O(H) because the stack stores the active root-to-leaf path.
    """
    result: List[int] = []
    stack: List[TreeNode] = []
    current = root

    while current is not None or stack:
        # Keep walking left so the next node popped is the inorder predecessor.
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
