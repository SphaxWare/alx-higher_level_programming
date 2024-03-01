#!/usr/bin/python3
"""
request to the URL and displays the value of the X-Request-Id
variable found in the header of the response
"""
import requests
import sys

if __name__ == "__main__":
    """Main module"""
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        requested_id = response.headers['X-Request-Id']
        print(requested_id)
