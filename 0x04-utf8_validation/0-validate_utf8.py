#!/usr/bin/python3
""" method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data: list) -> bool:
    """return True if data is a valid UTF-8 encoding,
    else return False"""
    if not data:
        return False

    followed_bytes = 0
    for i in data:
        if not isinstance(i, int) or i < 0 or i > 255:
            return False
        binary = format(i, '08b')

        if followed_bytes == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                followed_bytes = 1
            elif binary.startswith('1110'):
                followed_bytes = 2
            elif binary.startswith('11110'):
                followed_bytes = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
        followed_bytes -= 1

    return followed_bytes == 0
