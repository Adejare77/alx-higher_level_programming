#!/usr/bin/python3
""" function that prints a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    """ prints sorted dictionary using keys

        Args:
            a_dictionary: dictionary to be sorted
    """
    [print(f"{u}: {v}") for u, v in sorted(a_dictionary.items())]
