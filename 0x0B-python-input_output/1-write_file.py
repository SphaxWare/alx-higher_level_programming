#!/usr/bin/python3
"""write Module"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
