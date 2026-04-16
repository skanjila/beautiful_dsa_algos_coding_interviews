


class NAryTreeNode:
    """Simple N-ary tree node.

    Time complexity: O(1) to construct the node, aside from copying any
    provided children iterable.
    Space complexity: O(k) for storing k child references.
    """

    def __init__(self, val=0, children=None):
        self.val = val
        self.children = list(children) if children is not None else []
