#!/usr/bin/python3
""" Create an object from a JSON file """
import json


def load_from_json_file(filename):
    """ Create and return the obj """
    with open(filename, "r") as file:
        return json.load(file)
