#!/usr/bin/python3
# Takes in a URL and an email address, sends a POST request to the
# passed URL with the email as a parameter, and finally displays
# the body of the response

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    parameters = {'email': argv[2]}
    content = requests.post(url, data=parameters)
    # print(content.content.decode())
    print(content.text)
