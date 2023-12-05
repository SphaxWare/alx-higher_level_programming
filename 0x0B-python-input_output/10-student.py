#!/usr/bin/python3
"""Student module"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        obj = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                obj[k] = v
        return obj
