#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    parameter = {'email': argv[2]}
    data = parse.urlencode(parameter).encode('utf-8')
    post_resp = request.Request(url, method='POST', data=data)
    with request.urlopen(post_resp) as resp:
        content = resp.read().decode()
        print(content)
