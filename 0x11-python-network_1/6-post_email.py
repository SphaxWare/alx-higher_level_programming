#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
import sys


if __name__ == "__main__":
    """main Module"""
    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print("Your email is: {}".format(response.text))
