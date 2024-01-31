#!/usr/bin/python3
""" method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data: list) -> bool:
    """return True if data is a valid UTF-8 encoding,
    else return False"""
    if not data:
        return False

    followed_bytes = 0
    for value in data:
        if not isinstance(value, int) or value < 0 or value > 255:
            return False

        if followed_bytes == 0:
            if value >> 7 == 0:
                continue
            elif value >> 5 == 0b110:
                followed_bytes = 1
            elif value >> 4 == 0b1110:
                followed_bytes = 2
            elif value >> 3 == 0b11110:
                followed_bytes = 3
            else:
                return False
        else:
            if value >> 6 != 0b10:
                return False
        followed_bytes -= 1

    return followed_bytes == 0
