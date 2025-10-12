from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode

def max_depth_binary_tree_postorder(root: TreeNode) -> int:
    """Calculate the maximum depth of the binary tree, to do this
    we calculate the left depth, the right depth and then calculate the max
    depth of the tree
    @param root: The tree node representing the root of the binary tree
    @return: The maximum depth of the binary tree"""
    def dfs(node: TreeNode) -> int
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        return max(left_depth, right_depth) + 1
    return dfs(root)