#!/usr/bin/python3
""" function that prints all integers of a list
    in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    """ reverse a given list

    Args:
        my_list: list to be reversed
    """
    for r in my_list[-1::-1]:
        print("{:d}".format(r))
