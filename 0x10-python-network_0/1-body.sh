#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sI "$1" | grep "HTTP/1.1 200 OK" > /dev/null
if [ "$?" -eq 0 ]; then
	curl -s "$1"
fi
