#!/usr/bin/python3
"""append Module"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
