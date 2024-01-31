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
        binary = bin(i)
        if len(binary) > 10:
            return False
    return True
