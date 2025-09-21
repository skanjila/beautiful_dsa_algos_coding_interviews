# tests/trees/binary_tree/test_rightmost_node_binary_tree.py
from collections import deque

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode



def rightmost_node_binary_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    results = []

    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == level_size-1:
                results.append(node.val)
    return results