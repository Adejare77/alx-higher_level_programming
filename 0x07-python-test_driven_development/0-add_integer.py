#!/usr/bin/python3
"""
    Sum two integers(a and b) together,
    Return value should be an integer,
    float are first converted to integer before use

"""


def add_integer(a, b=98):
    """
        Returns sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
