from collections import deque
from typing import Optional

from .tree_node import TreeNode


class Codec:
    """
    Serialize and deserialize a binary tree in level-order form.

    Time complexity: O(N) for serialize and O(N) for deserialize because each
    node or null marker is processed a constant number of times.
    Space complexity: O(N) because the serialized tokens and queue can both grow
    with the number of nodes.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        tokens = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                tokens.append("#")
                continue

            tokens.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        # Drop trailing null markers because they do not add structure anymore.
        while tokens and tokens[-1] == "#":
            tokens.pop()

        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(tokens):
            node = queue.popleft()

            if index < len(tokens) and tokens[index] != "#":
                node.left = TreeNode(int(tokens[index]))
                queue.append(node.left)
            index += 1

            if index < len(tokens) and tokens[index] != "#":
                node.right = TreeNode(int(tokens[index]))
                queue.append(node.right)
            index += 1

        return root
