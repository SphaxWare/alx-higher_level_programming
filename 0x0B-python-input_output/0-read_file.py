#!/usr/bin/python3
"""Read Module"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
