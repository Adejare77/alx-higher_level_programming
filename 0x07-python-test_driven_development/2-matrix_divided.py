#!/usr/bin/python3
""" Matrix """


def matrix_divided(matrix, div):
    """ Divides all element of the matrix """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")

    new_matrix = matrix[:]

    _list = all([isinstance(t, list) for t in new_matrix if
                 isinstance(new_matrix, list)])
    if not (_list and new_matrix != []):
        raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")

    values = all([all([isinstance(k, (int, float)) for k in i])
                  for i in new_matrix])
    if not (values and new_matrix != [[]]):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    row_size = [len(u) for u in new_matrix]
    size = all([(row_size[0] == r) for r in row_size])
    if not size:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [([float(f"{v/div:0.2f}") for v in s]) for s in new_matrix]
    return new_matrix
