#!/usr/bin/python3
""" Creates object from a JSON string """

import json


def from_json_string(my_str):
    """ Return an object represented by JSON string """
    return json.loads(my_str)
