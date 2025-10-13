


class NAryTreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = list(children) if children is not None else []