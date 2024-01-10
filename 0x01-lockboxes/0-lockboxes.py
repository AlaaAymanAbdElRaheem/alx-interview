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

    keys = list(boxes[0])
    unlocked = [0]

    while keys:
        key = keys.pop()
        if key not in unlocked and key < len(boxes):
            unlocked.append(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
