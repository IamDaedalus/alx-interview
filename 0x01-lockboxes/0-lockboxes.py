#!/usr/bin/python3
"""
this module contains a function to determine if all the boxes can be opened.
"""

from typing import List, Set


def canUnlockAll(boxes: List[List]) -> bool:
    """Determine if all the boxes can be opened."""
    num_boxes: int = len(boxes)

    # initialise a List to represent state of each lockbox
    # all boxes are initially locked except the first one
    box_state: List[bool] = [False] * num_boxes
    # first box is always unlocked
    box_state[0] = True

    # initialise a set to keep track of visited boxes
    visited: Set[int] = set([0])

    # function to unlock boxes recursively
    def unlock_boxes(box_idx: int) -> None:
        # iterate through the keys in the current box
        for key in boxes[box_idx]:
            # if the key is valid and has not been visited unlock the box
            if key < num_boxes and key not in visited:
                # mark the box as visited and unlocked
                visited.add(key)
                # unlock the box
                box_state[key] = True
                # recursively unlock the boxes in the current box
                unlock_boxes(key)

    # start unlocking boxes from the first box
    unlock_boxes(0)

    # return True if all boxes are unlocked
    return all(box_state)
