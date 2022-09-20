#!/usr/bin/python3
"""
This module defines funtion that adds two integers. for example:
>>> add_integer(2, 3)
5
"""
def add_integer(a, b=98):
    """
    Returns a + b
    """
    _type = [int, float]
    try:
        if type(a) not in _type or type(b) not in _type:
            raise TypeError
        a + b
    except TypeError:
        if type(a) not in _type:
            print("a must be an integer")
        if type(b) not in _type:
            print("b must be an integer")
        return

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
