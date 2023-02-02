#!/usr/bin/python3
"""This module contains a function that implements the
lock boxes problem
"""


def canUnlockAll(boxes):
    """This function determines if all the boxes can be opened
    Args:
        boxes (list): a list of lists that contains keys that can or cannot
        open other boxes
    Return:
         True (boolean): if all boxes can be opened
         else
         False(boolean): if all boxes cannot be opened / some boxes
         can be opened
    """
    # boxes is a list of lists
    avail_keys = [0]

    for box in avail_keys:
        for key in boxes[box]:
            if key not in avail_keys and key < len(boxes):
                avail_keys.append(key)

    if len(avail_keys) == len(boxes):
        return True

    return False
