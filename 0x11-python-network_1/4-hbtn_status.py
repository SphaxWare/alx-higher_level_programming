#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    """Main module"""
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content_type = response.getheader('Content-Type')
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content_type)))
        print("\t- content: {}".format(content))
