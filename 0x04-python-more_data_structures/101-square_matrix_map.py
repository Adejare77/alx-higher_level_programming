#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x ** 2, l_)) for l_ in matrix if l_ != [[]]]
