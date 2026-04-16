from collections import deque
from typing import List, Optional

from .tree_node import TreeNode


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return level-order traversal while alternating direction per level.

    Time complexity: O(N) because each node is processed once.
    Space complexity: O(W) because the queue stores at most one level at a time.
    """
    if root is None:
        return []

    result: List[List[int]] = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            # Append on opposite sides so we avoid reversing after the level.
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result
