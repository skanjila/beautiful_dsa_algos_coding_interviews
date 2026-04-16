from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Return the largest connected island area in a binary grid.

    Time complexity: O(R * C)
    Space complexity: O(R * C) in the worst case from recursion depth.
    """

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    def dfs(row: int, col: int) -> int:
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 0
        if grid[row][col] != 1:
            return 0

        # Mark visited before exploring neighbors so the same land is not counted twice.
        grid[row][col] = 0
        return (
            1
            + dfs(row + 1, col)
            + dfs(row - 1, col)
            + dfs(row, col + 1)
            + dfs(row, col - 1)
        )

    best = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # DFS returns the area of the whole connected component.
                best = max(best, dfs(row, col))
    return best
