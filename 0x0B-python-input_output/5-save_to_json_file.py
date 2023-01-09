#!/usr/bin/python3
""" Write the JSON representation of an object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ Write the JSON reps of an obj to a file"""
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
