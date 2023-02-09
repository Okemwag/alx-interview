#!/usr/bin/python3
"""
- Minimum Operations
- Returns an integer
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    counter = 0
    h = 2

    if type(n) != int or n <= 0:
        return (0)

    while (n != 1):
        if n % h:
            h += 1
        else:
            n /= h
            counter += h
    return (counter)
