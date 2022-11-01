#!/usr/bin/python3
""" Save Object to a Json File """

import json
def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using JSON representation

        Args:
            my_obj(string): text object to be written in a file
            filename: name of the json file
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
