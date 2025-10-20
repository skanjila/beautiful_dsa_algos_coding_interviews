from typing import List


def unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> int:
    """
    Given an m x n grid (obstacleGrid) filled with 0s (empty spaces) and 1s (obstacles),
    return the number of unique paths from the top-left corner (0,0)
    to the bottom-right corner (m-1, n-1).

    You can only move either right or down at any point in time.

    This version uses DFS (Depth-First Search) with memoization (top-down DP).
    """

    # --- Step 1: Handle invalid input cases ---
    # If the grid is empty or the first row is empty, there are no paths.
    if not obstacleGrid or not obstacleGrid[0]:
        return 0

    # Dimensions of the grid
    rows_limit, cols_limit = len(obstacleGrid), len(obstacleGrid[0])

    # If the start or destination cell is blocked (value = 1),
    # then it’s impossible to reach the goal.
    if obstacleGrid[0][0] == 1 or obstacleGrid[rows_limit - 1][cols_limit - 1] == 1:
        return 0

    # --- Step 2: Memoization cache ---
    # This dictionary stores previously computed results:
    # key: (row, column)
    # value: number of unique paths from this cell to the bottom-right.
    memo = {}

    # --- Step 3: Recursive DFS function ---
    def dfs(row: int, column: int) -> int:
        """
        Explore all paths starting from (row, column)
        and return the total number of valid paths to reach the goal.
        """

        # --- Base Case 1: Out of bounds ---
        # If we move outside the grid boundaries, there’s no valid path.
        if row >= rows_limit or column >= cols_limit:
            return 0

        # --- Base Case 2: Hit an obstacle ---
        # A cell marked as 1 means blocked, so no valid path passes through it.
        if obstacleGrid[row][column] == 1:
            return 0

        # --- Base Case 3: Reached the destination ---
        # If we reach the bottom-right cell, that’s one valid path found.
        if (row, column) == (rows_limit - 1, cols_limit - 1):
            return 1

        # --- Base Case 4: Already computed ---
        # If we’ve already computed paths from this position, reuse the cached result.
        if (row, column) in memo:
            return memo[(row, column)]

        # --- Recursive Step ---
        # From the current cell, we can move either:
        #   → Right  (same row, next column)
        #   ↓ Down   (next row, same column)
        right_paths_to_explore = dfs(row, column + 1)
        down_paths_to_explore = dfs(row + 1, column)

        # --- Combine the results ---
        # The total number of paths from this cell is the sum of both moves.
        total_paths = right_paths_to_explore + down_paths_to_explore

        # Store this result in memo to avoid recomputation in future calls.
        memo[(row, column)] = total_paths

        # Return the total number of paths from this cell.
        return total_paths

    # --- Step 4: Start the DFS search ---
    # Begin exploring from the top-left corner (0, 0)
    return dfs(0, 0)
