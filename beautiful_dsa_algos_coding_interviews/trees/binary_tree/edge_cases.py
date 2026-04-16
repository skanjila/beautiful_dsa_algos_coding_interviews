from typing import List, Optional

from beautiful_dsa_algos_coding_interviews.trees.binary_tree.calc_diameter_with_depth import (
    calc_diameter_with_depth,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.invert_binary_tree_iterative import (
    invert_binary_tree_iterative,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.invert_binary_tree_recursive import (
    invert_binary_tree_recursive,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.is_balanced_with_depth import (
    is_balanced_with_depth,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.longest_univalue_path import (
    longest_univalue_path,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.lowest_common_ancestor import (
    lowest_common_ancestor,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.max_depth_postorder import (
    max_depth_binary_tree_postorder,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.right_side_view import (
    right_side_view,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.rightmost_node_binary_tree import (
    rightmost_node_binary_tree,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_paths import treePaths
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.validate_binary_tree import (
    is_valid_bst,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.vertical_order_traversal import (
    vertical_order_bfs,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.widest_binary_tree_level import (
    widest_binary_tree_level,
)


def tree_paths_with_edge_cases(root: Optional[object]) -> List[str]:
    """Guard wrapper for ``treePaths``.

    Time complexity: O(N * L) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return []
    return treePaths(None, root)


def rightmost_node_binary_tree_with_edge_cases(root: Optional[object]) -> List[int]:
    """Guard wrapper for right-side-view style BFS.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return []
    return rightmost_node_binary_tree(root)


def invert_binary_tree_iterative_with_edge_cases(root: Optional[object]) -> Optional[object]:
    """Guard wrapper for iterative tree inversion.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return None
    return invert_binary_tree_iterative(root)


def invert_binary_tree_recursive_with_edge_cases(root: Optional[object]) -> Optional[object]:
    """Guard wrapper for recursive tree inversion.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return None
    return invert_binary_tree_recursive(root)


def is_valid_bst_with_edge_cases(root: Optional[object]) -> bool:
    """Guard wrapper for BST validation.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return True
    return is_valid_bst(root)


def max_depth_postorder_with_edge_cases(root: Optional[object]) -> int:
    """Guard wrapper for postorder max-depth calculation.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return 0
    return max_depth_binary_tree_postorder(root)


def calc_diameter_with_edge_cases(root: Optional[object]) -> int:
    """Guard wrapper for tree diameter calculation.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return 0
    return calc_diameter_with_depth(root)


def is_balanced_with_depth_edge_cases(root: Optional[object]) -> bool:
    """Guard wrapper for balanced-tree checking.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return True
    return is_balanced_with_depth(root)


def longest_univalue_path_with_edge_cases(root: Optional[object]) -> int:
    """Guard wrapper for same-value path calculation.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return 0
    return longest_univalue_path(root)


def lowest_common_ancestor_with_edge_cases(
    root: Optional[object], p: Optional[object], q: Optional[object]
) -> Optional[object]:
    """Guard wrapper for LCA search.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None or p is None or q is None:
        return None
    return lowest_common_ancestor(root, p, q)


def right_side_view_with_edge_cases(root: Optional[object]) -> List[int]:
    """Guard wrapper for right-side-view traversal.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return []
    return right_side_view(root)


def vertical_order_bfs_with_edge_cases(root: Optional[object]) -> List[List[int]]:
    """Guard wrapper for vertical-order traversal.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return []
    return vertical_order_bfs(root)


def widest_binary_tree_level_with_edge_cases(root: Optional[object]) -> int:
    """Guard wrapper for width-by-level calculation.

    Time complexity: O(N)
    Space complexity: Same as the wrapped function.
    """
    if root is None:
        return 0
    return widest_binary_tree_level(root)
