from typing import List


def solve_surrounded_regions(board: List[List[str]]) -> None:
    """
    Capture surrounded regions in place by marking border-connected safe cells.

    Time complexity: O(R * C)
    Space complexity: O(R * C) in the worst case from recursion depth.
    """

    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    def dfs(row: int, col: int) -> None:
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if board[row][col] != "O":
            return

        # Mark border-connected regions as safe so they survive the final sweep.
        board[row][col] = "S"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for row in range(rows):
        dfs(row, 0)
        dfs(row, cols - 1)

    for col in range(cols):
        dfs(0, col)
        dfs(rows - 1, col)

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "O":
                # Any remaining O was never connected to a border, so it is captured.
                board[row][col] = "X"
            elif board[row][col] == "S":
                board[row][col] = "O"
