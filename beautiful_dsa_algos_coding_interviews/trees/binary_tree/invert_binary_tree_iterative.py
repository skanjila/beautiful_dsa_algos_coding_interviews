
class TreeNode:
    """Basic binary-tree node used by the iterative invert function.

    Time complexity: O(1) to construct.
    Space complexity: O(1) per node, excluding child subtrees.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invert_binary_tree_iterative(root: TreeNode) -> TreeNode:
    """Invert a binary tree using an explicit stack.

    Time complexity: O(N)
    Space complexity: O(H) to O(N) depending on tree shape.
    """
    if not root:
        return None
    stack = [root]

    while stack:
        popped_node = stack.pop()
        popped_node.left, popped_node.right = popped_node.right, popped_node.left

        if popped_node.left:
            stack.append(popped_node.left)
        if popped_node.right:
            stack.append(popped_node.right)
    return root
