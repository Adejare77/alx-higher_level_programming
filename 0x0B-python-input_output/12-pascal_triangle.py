#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the
        pascal triangle n

        Args:
            n: nth number of pascal list
    """
    if n <= 0:
        return []

