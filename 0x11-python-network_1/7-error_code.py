#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the response
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        # print(resp.content.decode())
        print(resp.text)
