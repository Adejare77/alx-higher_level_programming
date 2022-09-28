#!/usr/bin/python3
""" function that computes the square value of all
    integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    """ returns square of the matrix without changing
        the original matrix

        Args:
            matrix: 2 dimensional array
        Returns:
            same size as matrix,
            Each value should be the square of the value of
            the input
    """
    result = []
    if matrix != [[]]:
        for list_ in matrix:
            result.append(list(map(lambda x: x**2, list_)))
    return result
