#!/usr/bin/python3
""" This module defines a class 'Square'. """


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """ Initialize size. """
        self.__size = size

    def __eq__(self, other):
        """ Equal. """
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """ Not equal. """
        return not self.__eq__(other)

    def __lt__(self, other):
        """ Less than. """
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        """ Less than or equal. """
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        """ Get size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size to equal value. """
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return area of the square."""
        return self.__size ** 2
