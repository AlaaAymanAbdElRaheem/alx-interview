#!/usr/bin/python3
""" method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data: list) -> bool:
    """return True if data is a valid UTF-8 encoding,
    else return False"""
    if not data:
        return False
    for i in data:
        if not isinstance(i, int):
            return False
        binary = format(i, '08b')
        if len(binary) > 8 or len(binary) < 1:
            return False
        if binary.startswith('10'):
            return False
        if binary.startswith('0'):
            continue
        if binary.startswith('110'):
            bytes = 1
        elif binary.startswith('1110'):
            bytes = 2
        elif binary.startswith('11110'):
            bytes = 3
        else:
            return False
    return True
