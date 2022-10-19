#!/usr/bin/python3
""" Print Square """


def print_square(size):
    """ function that prints a square with a character `#` """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if (size < 0 and isinstance(size, int)):
        raise ValueError("size must be >= 0")
    if (size < 0 and isinstance(size, float)):
        raise TypeError("size must be an integer")
    for k in range(int(size)):
        print("#" * int(size))
