
class TreeNode:
    """Generic binary-tree node used across tree exercises.

    Time complexity: O(1) to construct.
    Space complexity: O(1) per node, excluding child subtrees.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
