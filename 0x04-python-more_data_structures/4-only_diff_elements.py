#!/usr/bin/python3
""" function that returns a set of all elements present
    in only one set
"""


def only_diff_elements(set_1, set_2):
    """ finds element(s) present in set_1 and set_2 but not
        present in both

        Args:
            set_1: first set
            set_2: second set
    """
    return (set_1.union(set_2) - set_1.intersection(set_2))
