#!/usr/bin/python3
""" function that deletes a key in a dictionary """


def simple_delete(a_dictionary, key=""):
    """ deletes a key in the dictionary

        Args:
            a_dictionary: dictionary to delete from
            key: key to be deleted
    """
    if a_dictionary.get(key) in a_dictionary.values():
        del a_dictionary[key]
    return a_dictionary
