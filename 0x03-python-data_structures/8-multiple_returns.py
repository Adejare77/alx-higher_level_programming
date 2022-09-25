#!/usr/bin/python3
""" function that returns a tuple with the length
    of a string and its first character
"""


def multiple_returns(sentence):
    """ returns first character and length of string

    Args:
        sentence: argument to find its first character and length

    Returns:
        length of string and first character of string
    """
    if sentence == "":
        return (len(sentence), None)
    return (len(sentence), sentence[0])
