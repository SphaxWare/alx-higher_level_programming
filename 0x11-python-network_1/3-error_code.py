#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    """Main module"""
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
