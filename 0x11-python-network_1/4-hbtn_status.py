#!/usr/bin/python3
""" Fetches 'https://alx-intranet.hbtn.io/status'
"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    content = resp.content.decode()
    print('Body response:', end="")
    print("\n\t- type:", type(content), end="")
    print("\n\t- content:", content)
