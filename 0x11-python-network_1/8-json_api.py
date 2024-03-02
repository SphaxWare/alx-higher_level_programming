#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    """Main Module"""
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    letter = {'q': q}
    response = requests.post(url, data=letter)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
