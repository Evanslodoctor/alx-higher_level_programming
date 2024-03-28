#!/usr/bin/python3
"""Fetch
https://intranet.hbtn.io/status
using urlib package
"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as r:
        res = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode("UTF-8")))
