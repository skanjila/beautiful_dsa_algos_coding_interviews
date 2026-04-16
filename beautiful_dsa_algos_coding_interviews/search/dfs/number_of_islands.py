from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    """
    Count connected land components in a binary grid using DFS flood fill.

    Time complexity: O(R * C)
    Space complexity: O(R * C) in the worst case from recursion depth.
    """

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(row: int, col: int) -> None:
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if grid[row][col] != "1":
            return

        # Sink the current land cell so we do not count it again.
        grid[row][col] = "0"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                # One DFS consumes exactly one connected island.
                islands += 1
                dfs(row, col)

    return islands
