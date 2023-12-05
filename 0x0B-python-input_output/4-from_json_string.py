#!/usr/bin/python3
""" JSON string to Object """
import json


def from_json_string(my_str):
    """ change JSON string to a Python Object

        Args:
            my_str (str): Json string to be represented in object

        Return:
            an object(Python data Structure)
    """
    return json.loads(my_str)
