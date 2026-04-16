from typing import List, Optional

from .tree_node import TreeNode


def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Return all root-to-leaf paths whose values sum to the target.

    Time complexity: O(N * H) in the worst case because each node is visited
    once and each successful path copy can cost up to tree height H.
    Space complexity: O(H) recursion depth, excluding the returned paths.
    """
    result: List[List[int]] = []
    current_path: List[int] = []

    def dfs(node: Optional[TreeNode], running_sum: int) -> None:
        if node is None:
            return

        current_path.append(node.val)
        running_sum += node.val

        if node.left is None and node.right is None and running_sum == target_sum:
            result.append(current_path[:])
        else:
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)

        # Backtrack so sibling branches reuse the same path list safely.
        current_path.pop()

    dfs(root, 0)
    return result
