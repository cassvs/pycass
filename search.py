# search.py
# Searching algorithms

import math

# Linear search
def linear(target, list):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1
# End of linear function

# Binary search
def binary(target, list):
    l = 0
    r = len(list) - 1
    while l <= r:
        index = math.floor((l + r) / 2)
        if list[index] < target:
            l = index + 1
        elif list[index] > target:
            r = index - 1
        else:
            return index
    return -1
# End of binary function
