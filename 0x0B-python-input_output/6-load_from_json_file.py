#!/usr/bin/python3
""" Create Object from a JSON file """

import json
def load_from_json_file(filename):
    """ Creates an object from a "JSON file

        Args:
            filename: name of the json file
    """
    with open(filename, 'r', encoding='utf-8') as fr:
        return json.load(fr)
