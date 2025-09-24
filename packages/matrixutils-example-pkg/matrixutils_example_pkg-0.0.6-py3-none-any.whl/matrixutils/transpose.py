from typing import List

Matrix = List[List[float]]

def matrix_transpose(m: Matrix) -> Matrix:
    """Return transpose of the matrix.

    Example:
        >>> matrix_transpose([[1,2,3],[4,5,6]])
        [[1,4],[2,5],[3,6]]
    """
    if not m:
        return []
    if not all(isinstance(row, list) for row in m):
        raise ValueError("Matrix must be a list of rows")
    # ensure rectangular
    cols = len(m[0])
    if any(len(row) != cols for row in m):
        raise ValueError("All rows must have the same length")
    return [[m[r][c] for r in range(len(m))] for c in range(cols)]
