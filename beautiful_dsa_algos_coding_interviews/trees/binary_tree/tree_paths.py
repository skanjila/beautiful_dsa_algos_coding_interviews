from typing import List, Optional


def treePaths(_: object, root: Optional[object]) -> List[str]:
    """
    Return all root-to-leaf paths for the given tree.

    The tests pass an N-ary node type here, so the implementation only relies on
    `.val` and `.children` instead of a specific binary-tree shape.

    Time complexity: O(N * L), where L is the average path-string assembly cost.
    Space complexity: O(H) recursion depth, excluding output.
    """

    if root is None:
        return []

    results: List[str] = []

    def dfs(node: object, path: List[str]) -> None:
        """Depth-first traversal that accumulates one root-to-leaf path.

        Time complexity: O(size of subtree)
        Space complexity: O(H) recursion depth.
        """
        if node is None:
            return

        next_path = path + [str(node.val)]
        children = [child for child in getattr(node, "children", []) if child is not None]
        if not children:
            results.append("->".join(next_path))
            return

        for child in children:
            dfs(child, next_path)

    dfs(root, [])
    return results
