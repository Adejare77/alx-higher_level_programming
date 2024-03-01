#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and displays the body
# of the response (decoded in utf-8)

from urllib import error
from urllib import request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as resp:
            content = resp.read().decode()
            print(content)
    except error.HTTPError as err:
        print("Error code:", err)
