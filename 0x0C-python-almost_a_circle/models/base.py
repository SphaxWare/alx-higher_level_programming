#!/usr/bin/python3
"""base module"""
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            elif cls is Square:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """load from a csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        try:
            filename = cls.__name__ + ".csv"
            objs = []
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                for line in reader:
                    line = [int(n) for n in line]
                    if cls is Rectangle:
                        dic = {"id": line[0], "width": line[1],
                               "height": line[2], "x": line[3], "y": line[4]}
                    elif cls is Square:
                        dic = {"id": line[0], "size": line[1],
                               "x": line[2], "y": line[3]}
                    objs.append(cls.create(**dic))
            return objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        rainbow = ["red", "orange", "yellow",
                   "green", "blue", "indigo", "violet"]
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.speed(100)
        for shape in list_rectangles:
            t.setheading(0)
            t.penup()
            t.goto(shape.x, shape.y)
            t.pendown()
            t.pencolor(rainbow[random.randint(0, 6)])
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            t.left(90)
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
        for shape in list_squares:
            t.setheading(0)
            t.penup()
            t.goto(shape.x, shape.y)
            t.pendown()
            t.pencolor(rainbow[random.randint(0, 6)])
            for i in range(4):
                t.forward(shape.size)
                t.left(90)
        turtle.done()
