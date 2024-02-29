#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response
cut -d ' ' -zf 2 <<< "$(grep -i 'http' <<< $(curl -sI "$1"))"
