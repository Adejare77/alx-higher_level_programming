#!/usr/bin/python3
""" function that replaces all occurrences of an element
    by another in a new list.
"""


def search_replace(my_list, search, replace):
    """ search and replace element of a list

        Args:
            my_list: is the initial list
            search: is the element to replace in the list
            replace: is the new element

        return:
            new_list
    """

    new_list = my_list.copy()
    if new_list != []:
        for index, element in enumerate(new_list):
            if element == search:
                new_list[index] = replace
    return new_list
