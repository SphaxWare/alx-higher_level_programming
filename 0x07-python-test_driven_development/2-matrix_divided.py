#!/usr/bin/python3
"""
    matrix devider module.
"""


def matrix_divided(matrix, div):
    """
    this function take a matrix and a number(int or float)
    and divide each number in this matrix by that number

     Args:
        matrix: List of lists containing int or float
        div: number to divide matrix by
    Returns:
        list: List of lists representing divided matrix.
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(col, (int, float)) for row in matrix for col in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    newmat = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newmat[i].append(round(matrix[i][j] / div, 2))
    return newmat
