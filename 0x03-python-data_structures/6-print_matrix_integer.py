#!/usr/bin/python3
""" function that prints a matrix of integers """


def print_matrix_integer(matrix=[[]]):
    """ print a matrix of integers

        Args:
            matrix: matrix shape
    """
    for i in matrix:
        for k in i:
            if (k != i[-1]):
                print(f"{k}", end=" ")
            else:
                print("{k}")
