#!/usr/bin/python3
"""Load Json Module"""


import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
