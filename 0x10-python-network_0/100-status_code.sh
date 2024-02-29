#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code
# of the response

curl -sI "$1" | gerep -i "http" | cut -d " " -zf 2
