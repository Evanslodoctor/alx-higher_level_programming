#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        # list comprehension syntax -> [expression for item in items]
        [print("{:d}".format(item)) for item in reversed(my_list)]
