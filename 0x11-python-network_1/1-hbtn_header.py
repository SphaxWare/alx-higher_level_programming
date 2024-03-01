#!/usr/bin/python3
"""
request to the URL and displays the value of the X-Request-Id
variable found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    """Main module"""
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        requested_id = response.getheader('X-Request-Id')
        print(requested_id)
