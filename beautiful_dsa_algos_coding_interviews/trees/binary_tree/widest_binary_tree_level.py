from collections import deque

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode


def widest_binary_tree_level(root: TreeNode) -> int:
    """
    Return the maximum width across all levels using positional indices.

    Time complexity: O(N)
    Space complexity: O(W)
    """

    if root is None:
        return 0

    best = 0
    queue = deque([(root, 0)])

    while queue:
        level_size = len(queue)
        _, first_index = queue[0]
        last_index = first_index
        for _ in range(level_size):
            node, index = queue.popleft()
            normalized = index - first_index
            last_index = normalized
            if node.left:
                queue.append((node.left, 2 * normalized))
            if node.right:
                queue.append((node.right, 2 * normalized + 1))
        best = max(best, last_index + 1)

    return best
