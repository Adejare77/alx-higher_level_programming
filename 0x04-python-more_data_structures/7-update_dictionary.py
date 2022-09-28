#!/usr/bin/python3
""" function that replaces or adds key/value in a dictionary """


def update_dictionary(a_dictionary, key, value):
    """ update or add key/value to a dictionary

        Args:
            key: argument will always be a string
            value: argument will be any type
    """
    a_dictionary[key] = value
    return a_dictionary
