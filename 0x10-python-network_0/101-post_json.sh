#!/bin/bash
# Sends a JSON POST request to a URL passed as first argument, and displays the
# body of the response
# Where the second argument is a JSON File
curl -sH "Content-Type: application/json" -X POST -d "$(cat "$2")" "$1"
