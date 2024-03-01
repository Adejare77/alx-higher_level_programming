#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
'http://0.0.0.0:5000/search_user' with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == '__main__':
    value = "" if len(argv) == 1 else argv[1]
    data = {"q": value}
    url = 'http://0.0.0.0:5000/search_user'
    resp = requests.post(url, data=data)

    try:
        json_format = resp.json()
        if json_format == {}:
            print("No result")
        else:
            print(f'[{json_format.get("id")}] {json_format.get("name")}')
    except Exception:
        print("Not a valid JSON")
