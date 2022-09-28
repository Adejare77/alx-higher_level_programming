#!/usr/bin/python3
""" function that returns a key with the biggest integer value """


def best_score(a_dictionary):
    """ Returns key with the biggest integer value in a dict """
    if a_dictionary is not None:
        max_v = max(list(a_dictionary.values()))
        for k, v in a_dictionary.items():
            if v == max_v:
                return k
    return None
