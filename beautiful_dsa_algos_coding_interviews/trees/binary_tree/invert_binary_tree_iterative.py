
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invert_binary_tree_iterative(root: TreeNode) -> TreeNode:
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