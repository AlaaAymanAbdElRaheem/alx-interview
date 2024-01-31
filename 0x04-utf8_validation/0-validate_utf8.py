#!/usr/bin/python3
""" method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data: list) -> bool:
    """return True if data is a valid UTF-8 encoding,
    else return False"""
    if not data:
        return False

    bytes_list = []
    for i in data:
        if not isinstance(i, int):
            return False
        binary = format(i, '08b')
        if len(binary) > 8 or len(binary) < 1:
            return False
        if binary.startswith('0'):
            continue
        if binary.startswith('10'):
            bytes_list.append(1)
        elif binary.startswith('110'):
            bytes_list.append(2)
        elif binary.startswith('1110'):
            bytes_list.append(3)
        elif binary.startswith('11110'):
            bytes_list.append(4)
        else:
            return False

    return sum(bytes_list) <= 4
