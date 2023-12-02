import numpy as np
from typing import List

def determinant(matrix: List[List[float]]) -> float:
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (List[List[float]]): A square matrix represented as a list of lists of floats.

    Returns:
        float: The determinant of the matrix, rounded to the nearest integer.

    Raises:
        ValueError: If the input is not a square matrix.
    """
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")

    return np.linalg.det(matrix).round(0)




m1 = [[4, 6], [3,8]]

m5 = [[2,4,2],[3,1,1],[1,2,0]]

a = determinant([[5]]) # , 5, "Determinant of a 1 x 1 matrix yields the value of the one element")
b = determinant(m1) #, 14, "Should return 4*8 - 3*6, i.e. 14")
c = determinant(m5) #, 10, "Should return the determinant of [[2,4,2],[3,1,1],[1,2,0]], i.e. 10")