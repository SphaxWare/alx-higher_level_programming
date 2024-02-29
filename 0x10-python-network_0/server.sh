#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Check if the server is running
curl -IsS "$1" > /dev/null
if [ "$?" -ne 0 ]; then
    echo "Error: Unable to connect to the server."
    exit 1
fi

# Extract the size of the body using curl and display it
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

