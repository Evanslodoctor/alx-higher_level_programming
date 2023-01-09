#!/usr/bin/python3
""" View JSON string representation of an object """

import json


def to_json_string(my_obj):
    """ Return a JSON representation of my_obj"""
    return json.dumps(my_obj)
