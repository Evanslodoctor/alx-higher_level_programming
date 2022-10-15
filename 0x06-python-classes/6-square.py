#!/usr/bin/python3
""" This module defines a class 'Square' """


class Square:
    """ Definition of a square by its size. """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize size and position attributes. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set size to equal value. """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get position. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position to equal value. """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return the area of the square. """
        return self.__size ** 2

    def my_print(self):
        """ Print the square with the character #. """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
