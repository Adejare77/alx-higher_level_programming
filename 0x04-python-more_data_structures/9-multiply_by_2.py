#!/usr/bin/python3
""" function that returns a new dictionary with all values
    multiplied by 2 """


def multiply_by_2(a_dictionary):
    """ multiply values in the dictionary by 2

        Args:
            a_dictionary: the dictionary
    """
    new_dictionary = \
        zip(a_dictionary.keys(), map(lambda x: x*2, a_dictionary.values()))
    return dict(new_dictionary)
