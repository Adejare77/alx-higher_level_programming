#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and displays the value
# of the variable X-Request-Id in the response header

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    resp = requests.get(url)
    resp_header = resp.headers
    # print(resp_header.get('X-Request-Id'))
    print(resp_header['X-Request-Id'])
