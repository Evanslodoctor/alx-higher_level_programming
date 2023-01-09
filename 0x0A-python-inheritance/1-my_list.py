#!/usr/bin/python3
""" This module extends the list class """


class MyList(list):
    """ Inherit from list class """

    def print_sorted(self):
        """ Print a sorted list """
        print(sorted(self))
