#!/usr/bin/python3
""" Provides a Base class for other classes """

import json
# import turtle


class Base:
    """ Definition of Base class """
    HEADERS = ("id")

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiate a base object """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string rep. of the dicts """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a JSON string rep of list_objs to a file """
        if not list_objs:
            text = "[]"
        else:
            text = cls.to_json_string([obj.to_dictionary()
                                      for obj in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(text)

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of JSON string representation """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all atrributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                return [cls.create(**obj)
                        for obj in cls.from_json_string(file.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to a CSV file """
        with open(f"{cls.__name__}.csv", "w") as file:
            if list_objs:
                for obj in list_objs:
                    obj = obj.to_dictionary()
                    file.write(
                        ",".join(str(obj[key]) for key in cls.HEADERS) + "\n"
                    )

    @classmethod
    def load_from_file_csv(cls):
        """ Load from a CSV file """
        try:
            with open(f"{cls.__name__}.csv", "r") as file:
                return [cls.create(
                    **{k: int(v) for k, v in zip(cls.HEADERS,
                        line.split(","))}
                ) for line in file.readlines()]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw the rectangles and squares """
        shapes = []
        if list_rectangles:
            shapes.extend(list_rectangles)
        if list_squares:
            shapes.extend(list_squares)
        pen = turtle.Turtle()
        pen.pen(pencolor='black', pendown=False, pensize=2, shown=False)
        for shape in shapes:
            pen.penup()
            pen.setpos(shape.x, shape.y)
            pen.pendown()
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
