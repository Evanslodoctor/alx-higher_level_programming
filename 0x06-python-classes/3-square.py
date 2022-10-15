#!/usr/bin/python3

"""Class represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: def area(self). """


class Square:
    """ Definition of a Square class with area attribute
     and private instance attribute, size. """

    def __init__(self, size=0):
        """ Initializing the instance attribute size with validation."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of the square. """
        return self.__size ** 2
