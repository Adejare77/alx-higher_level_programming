#!/usr/bin/python3
"""function that prints all integers of a list """

def print_list_integer(my_list=[]):
    """ prints all integer of a list

    Args:
        my_list: list to be printed out
    """
    for k in my_list:
        print("{}".format(k))