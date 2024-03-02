#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    """Main module"""
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
