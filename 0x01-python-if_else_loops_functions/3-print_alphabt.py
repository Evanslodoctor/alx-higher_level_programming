#!/usr/bin/python3
for a in range(97, 97 + 26):
    if a == 113 or a == 101:
        continue
    print("{:c}".format(a), end='')
