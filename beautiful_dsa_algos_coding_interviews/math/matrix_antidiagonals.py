

def get_antidiagonals(matrix):
    """
    Computes the antidiagonals of a given matrix.

    Antidiagonals run from the bottom-left to the top-right.

    Args:
        matrix: A 2D list representing the matrix.

    Returns:
        A list of lists, where each inner list represents an antidiagonal.
        Returns an empty list if the input matrix is empty.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    # The number of antidiagonals is (rows + cols - 1).
    # Initialize a list of lists to store the antidiagonals.
    antidiagonals = [[] for _ in range(rows + cols - 1)]

    # Iterate through each element of the matrix.
    for r in range(rows):
        for c in range(cols):
            # The sum of the row and column indices (r + c) is constant for each antidiagonal.
            # This sum is used as the index for the antidiagonals list.
            antidiagonals[r + c].append(matrix[r][c])

    return antidiagonals