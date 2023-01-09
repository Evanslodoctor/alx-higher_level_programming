#!/usr/bin/python3
""" Defines a class Student """


class Student:
    """ Definition of a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return a dict reps of a Student"""
        return self.__dict__
