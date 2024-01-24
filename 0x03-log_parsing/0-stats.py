#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


import sys
import re


if __name__ == "__main__":
    """ script that reads stdin line by line and computes metrics"""
    counter = 0
    size = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                   "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            match = re.match(
                r"(.*) - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d+) (.*)",
                line)
            if match:
                counter += 1
                size += int(match.group(3))
                if match.group(2) in status_code:
                    status_code[match.group(2)] += 1

            if counter == 10:
                print("File size: {}".format(size))
                for key, value in sorted(status_code.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
                counter = 0
                size = 0
                for key, value in sorted(status_code.items()):
                    status_code[key] = 0

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key, value in sorted(status_code.items()):
            if value != 0:
                print("{}: {}".format(key, value))
        raise
