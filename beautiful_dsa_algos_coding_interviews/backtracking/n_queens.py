from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Return every valid n-queens board using row-by-row backtracking.

    Time complexity: O(N!) in the worst case because each row branches across
    the remaining legal columns.
    Space complexity: O(N) for recursion depth and constraint sets, excluding
    output boards.
    """

    if n <= 0:
        return []

    results: List[List[str]] = []
    board = [["."] * n for _ in range(n)]
    used_columns = set()
    used_diag_down = set()
    used_diag_up = set()

    def backtrack(row: int) -> None:
        if row == n:
            results.append(["".join(board_row) for board_row in board])
            return

        for column in range(n):
            diag_down = row - column
            diag_up = row + column
            if (
                column in used_columns
                or diag_down in used_diag_down
                or diag_up in used_diag_up
            ):
                continue

            board[row][column] = "Q"
            used_columns.add(column)
            used_diag_down.add(diag_down)
            used_diag_up.add(diag_up)

            backtrack(row + 1)

            board[row][column] = "."
            used_columns.remove(column)
            used_diag_down.remove(diag_down)
            used_diag_up.remove(diag_up)

    backtrack(0)
    return results
