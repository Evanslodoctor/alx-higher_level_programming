#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
