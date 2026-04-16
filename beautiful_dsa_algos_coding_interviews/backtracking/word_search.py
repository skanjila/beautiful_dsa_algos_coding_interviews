from typing import List


def word_search(board: List[List[str]], word: str) -> bool:
    """
    Return True when ``word`` can be formed by adjacent horizontal/vertical cells.

    Time complexity: O(R * C * 4^L) in the worst case, where R and C are board
    dimensions and L is the word length.
    Space complexity: O(L) for recursion depth.
    """

    if not board or not board[0]:
        return word == ""
    if word == "":
        return True

    rows = len(board)
    cols = len(board[0])

    def dfs(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"
        found = (
            dfs(row + 1, col, index + 1)
            or dfs(row - 1, col, index + 1)
            or dfs(row, col + 1, index + 1)
            or dfs(row, col - 1, index + 1)
        )
        board[row][col] = temp
        return found

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    return False
