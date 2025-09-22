# anti_diagonals.py

from typing import List

def get_matrices_antidiagonals(matrix: List[List[int]]):
    """
    Return the anti-diagonals of a 2D matrix (row+col is constant along each anti-diagonal).

    Raises:
        IndexError: if the matrix is empty ([]) or first row has no columns ([[]]).
    """
    # Robust empty checks that work for lists and list-like objects.
    try:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            raise IndexError("Empty matrix")
    except (TypeError, IndexError):  # e.g., matrix is not subscriptable or matrix[0] missing
        raise IndexError("Empty matrix")

    rows = len(matrix)
    cols = len(matrix[0])
    antidiagonals = [[] for _ in range(rows + cols - 1)]

    for i in range(rows):
        for j in range(cols):
            antidiagonals[i + j].append(matrix[i][j])

    return antidiagonals
