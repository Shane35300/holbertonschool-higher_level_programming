#!/usr/bin/python3
"""
it's a function that divides all elements of a matrix
matrix must be a list of lists of integers or floats
Each row of the matrix must be of the same size
All elements of the matrix should be divided by div, rounded to 2 decimal
places
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """:param matrix: is the original matrix
    :param div: is the divider
    :return: a new matrix where each element is divided by div"""
    if (matrix is None or len(matrix) == 0):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not (isinstance(elem, int) or isinstance(elem, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    copy = []
    for row in matrix:
        copy_line = []
        for elem in row:
            nb = round(float(elem / div), 2)
            copy_line.append(nb)
        copy.append(copy_line)

    return copy
