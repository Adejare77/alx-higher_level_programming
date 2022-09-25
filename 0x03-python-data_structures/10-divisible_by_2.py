#!/usr/bin/python3
""" This finds the multiples of 2
"""

def divisible_by_2(my_list=[]):
    """ function that finds muliples of 2 in a list

        Args:
            my_list = list to search through

        Return:
            list of boolean expression (True or false)
    """
    bool_list = []
    for i in my_list:
        if i % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
