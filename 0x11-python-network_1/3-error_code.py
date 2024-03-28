#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body..
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    f = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(f) as resp:
            print(resp.read().decode("ascii"))
    except
        with urllib.error.HTTPError as e:
            printf("Error code: {}".format(e.code))
