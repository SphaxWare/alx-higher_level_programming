#!/usr/bin/python3
"""
    text indentation module.
"""


def text_indentation(text):
    """Text indentation function.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for delimiter in "?:.":
        text = (delimiter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimiter)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
