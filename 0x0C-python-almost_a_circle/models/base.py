#!/usr/bin/python3
"""base module"""
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """instanciate a class from a dict"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            instance = Rectangle(2, 4)
        elif cls is Square:
            instance = Square(2)
        else:
            instance = None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a file"""
        filename = cls.__name__+".json"
        try:
            with open(filename, 'r') as f:
                data = cls.from_json_string(f.read())
                instances = [cls.create(**d) for d in data]
                return instances
        except FileNotFoundError:
            return []
