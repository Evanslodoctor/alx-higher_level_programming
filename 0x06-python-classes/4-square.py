#!/usr/bin/python3
""" This module defines a class 'Square' """


class Square:
    """ Definition of a square by its size. """

    def __init__(self, size=0):
        """ Initialize size attribute. """
        self.__size = size

    @property
    def size(self):
        """ size retriever. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set size to equal value. """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square. """
        return self.__size ** 2
