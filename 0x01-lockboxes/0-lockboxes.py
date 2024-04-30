#!/usr/bin/python3
""" Module for 0-lockboxes"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    unlocked_boxes = set(boxes[0])
    visited = set()

    while unlocked_boxes:
        box = unlocked_boxes.pop()
        visited.add(box)

        for key in boxes[box]:
            if key not in visited:
                unlocked_boxes.add(key)

    return len(visited) == len(boxes)
