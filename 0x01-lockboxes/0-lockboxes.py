#!/usr/bin/python3
"""defines a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened
    Args:
        boxes: is a list of lists
    Returns:
        True if all boxes can be opened, else return False"""
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    keys = boxes[0].copy()
    count = 0

    for key in keys:
        if boxes[key] == []:
            count += 1
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)

    return len(keys)+count == len(boxes)
