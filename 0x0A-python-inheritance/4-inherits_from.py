#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """returns True or False"""
    return isinstance(obj, a_class) and type(obj) != a_class
