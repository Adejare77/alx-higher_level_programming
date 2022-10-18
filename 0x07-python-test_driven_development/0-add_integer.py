#!/usr/bin/python3
"""
    Sum two integers together
"""


def add_integer(a, b: int=98):
    """ Returns sum of a and b """
    if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return int(a + b)
