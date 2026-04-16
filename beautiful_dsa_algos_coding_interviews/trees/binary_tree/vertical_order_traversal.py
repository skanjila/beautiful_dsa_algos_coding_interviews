from collections import defaultdict, deque
from typing import List

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def vertical_order_bfs(root: TreeNode) -> List[List[int]]:
    """
    Return vertical order traversal using BFS to preserve top-down ordering.

    Time complexity: O(N)
    Space complexity: O(N)
    """

    if root is None:
        return []

    columns = defaultdict(list)
    queue = deque([(root, 0)])
    min_col = max_col = 0

    while queue:
        node, column = queue.popleft()
        columns[column].append(node.val)
        min_col = min(min_col, column)
        max_col = max(max_col, column)
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))

    return [columns[column] for column in range(min_col, max_col + 1)]
