#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
if curl -sI "$1" | grep -q "HTTP/1.1 200 OK"; then
    curl -s "$1"
fi
