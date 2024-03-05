#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
from sys import argv
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    resp = requests.get(url, auth=(argv[1], argv[2]))

    if resp.status_code == 200:
        json_data = resp.json()
        print(json_data['id'])
    else:
        print("None")
