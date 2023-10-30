#!/usr/bin/python3

""" The following module divides all elements of a matrix.
    check if Matrix is a list of lists, and have matching row size.
"""


def matrix_divided(matrix, div):

    """
    matrix_divided: Checks the following and divides all element by div.
    1. Each row of the matrix is the same size, otherwise
    raise a TypeError
    2. Each matrix element is an integer, otherwise
    raises a TypeError
    3. div is an integer or zero, otherwise
    raises TypeError or ZeroDivisionError
    """

    result_matrix = []

    if not matrix or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for i in matrix:
        if isinstance(i, list) and len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    for i in matrix:
        len_matrix = len(matrix[0])
        if len_matrix != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif isinstance(div, (float, int)):
        for i in matrix:
            row = []
            for j in i:
                row.append(round(j / div, 2))
            result_matrix.append(row)
        return result_matrix
    else:
        raise TypeError("div must be a number")