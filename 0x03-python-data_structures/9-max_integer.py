#!/usr/bin/python3
""" Finds the biggest integer of a list
"""


def max_integer(my_list=[]):
    """ finds the highest number in the list

        Args:
            my_list = list to search through
    """
    if my_list:
        max_ = my_list[0]
        for i in my_list:
            if i > max_:
                max_ = i
        return max_
