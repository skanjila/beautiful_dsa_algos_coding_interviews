from collections import deque
from typing import List

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def right_side_view(root: TreeNode) -> List[int]:
    """
    Return the visible node value from the right side at each level.

    Time complexity: O(N)
    Space complexity: O(W), where W is the maximum tree width.
    """

    if root is None:
        return []

    result: List[int] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for index in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if index == level_size - 1:
                result.append(node.val)
    return result
