from collections import deque
from typing import List, Optional

from .tree_node import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return the node values level by level from top to bottom.

    Time complexity: O(N) because each node enters and leaves the queue once.
    Space complexity: O(W) because the queue can hold one full tree level, where
    W is the maximum width.
    """
    if root is None:
        return []

    result: List[List[int]] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_values: List[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(level_values)

    return result
