#!/usr/bin/python3
""" This module defines a class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Definition of Rectangle class """
    HEADERS = ('id', 'width', 'height', 'x', 'y')

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiate a rectangle object """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ Return a str rep. of the rectangle """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
        return s

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get x attr """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x attr """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get y attr """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y attr """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Print the rectangle with the character '#' """
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.width] * self.height))

    def update(self, *args, **kwargs):
        """ Assign an arg to each attr """
        if args:
            for pair in zip(self.HEADERS, args):
                setattr(self, *pair)
        else:
            for key in kwargs:
                if key in self.HEADERS:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Return a dict representation of a rectangle """
        return {key: getattr(self, key) for key in Rectangle.HEADERS}
