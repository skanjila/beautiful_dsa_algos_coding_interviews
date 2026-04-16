from typing import List

from beautiful_dsa_algos_coding_interviews.graphs.can_finish import can_finish_kahn
from beautiful_dsa_algos_coding_interviews.graphs.can_finish_dfs import can_finish_dfs
from beautiful_dsa_algos_coding_interviews.graphs.connected_components import (
    findConnectedComponents,
)
from beautiful_dsa_algos_coding_interviews.graphs.unique_paths import (
    unique_paths_with_obstacles,
)


def can_finish_kahn_with_edge_cases(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Guard wrapper for Kahn's topological-sort solution.

    Time complexity: O(V + E) after constant-time early returns.
    Space complexity: Same as the wrapped function.
    """
    if num_courses <= 1:
        return True
    if not prerequisites:
        return True
    return can_finish_kahn(num_courses, prerequisites)


def can_finish_dfs_with_edge_cases(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Guard wrapper for DFS cycle detection.

    Time complexity: O(V + E) after constant-time early returns.
    Space complexity: Same as the wrapped function.
    """
    if num_courses <= 1:
        return True
    if not prerequisites:
        return True
    return can_finish_dfs(num_courses, prerequisites)


def connected_components_with_edge_cases(is_connected: List[List[int]]) -> int:
    """Guard wrapper for connected-components counting.

    Time complexity: O(N^2) for non-empty adjacency matrices.
    Space complexity: Same as the wrapped function.
    """
    if not is_connected:
        return 0
    return findConnectedComponents(is_connected)


def unique_paths_with_obstacles_edge_cases(obstacle_grid: List[List[int]]) -> int:
    """Guard wrapper for obstacle-grid path counting.

    Time complexity: O(R * C) for non-empty grids.
    Space complexity: Same as the wrapped function.
    """
    if not obstacle_grid or not obstacle_grid[0]:
        return 0
    return unique_paths_with_obstacles(obstacle_grid)
