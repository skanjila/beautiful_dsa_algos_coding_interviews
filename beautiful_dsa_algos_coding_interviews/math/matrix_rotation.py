from typing import List

def rotate_image(matrix: List[List[int]]) -> None:
    """
    Rotate an n×n matrix 90° clockwise in place.
    - Returns None (in-place)
    - Raises ValueError for non-square or ragged inputs
    - Treats [] as a no-op (returns None)
    """
    # Empty matrix: allow as no-op (adjust if your spec requires raising)
    if matrix == []:
        return None

    # Validate: list of lists, square, no ragged rows
    if not isinstance(matrix, list) or any(not isinstance(r, list) for r in matrix):
        raise ValueError("Matrix must be a list of lists.")

    n = len(matrix)
    if any(len(r) != n for r in matrix):
        raise ValueError("Matrix must be square (n x n) with equal row lengths.")

    # Transpose in place (skip diagonal to avoid redundant swaps)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in place
    for row in matrix:
        row.reverse()

    return None
