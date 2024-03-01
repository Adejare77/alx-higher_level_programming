#!/usr/bin/python3
""" script that fetches 'https://alx-intranet.hbtn.io/status'
"""

from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as resp:
        content = resp.read()
        print('Body response:', end="")
        print("\n    - type:", type(content), end="")
        print("\n    - content:", content, end="")
        print("\n    - utf8 content:", content.decode())
