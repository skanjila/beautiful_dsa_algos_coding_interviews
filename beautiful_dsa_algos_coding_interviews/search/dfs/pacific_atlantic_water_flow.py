from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Return coordinates that can reach both the Pacific and Atlantic oceans.

    Time complexity: O(R * C)
    Space complexity: O(R * C)
    """

    if not heights or not heights[0]:
        return []

    rows = len(heights)
    cols = len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(row: int, col: int, visited: set[tuple[int, int]], prev_height: int) -> None:
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if (row, col) in visited:
            return
        if heights[row][col] < prev_height:
            return

        # Reverse the usual water-flow thinking: start from an ocean border and
        # move only to cells that are high enough to flow back down to it.
        visited.add((row, col))
        current_height = heights[row][col]
        dfs(row + 1, col, visited, current_height)
        dfs(row - 1, col, visited, current_height)
        dfs(row, col + 1, visited, current_height)
        dfs(row, col - 1, visited, current_height)

    for row in range(rows):
        dfs(row, 0, pacific, heights[row][0])
        dfs(row, cols - 1, atlantic, heights[row][cols - 1])

    for col in range(cols):
        dfs(0, col, pacific, heights[0][col])
        dfs(rows - 1, col, atlantic, heights[rows - 1][col])

    # Cells visited from both boundary searches can reach both oceans.
    return [[row, col] for row, col in sorted(pacific & atlantic)]
