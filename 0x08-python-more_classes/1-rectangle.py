#!/usr/bin/python3
"""
This module defines Rectangle object
"""


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if type(value) != int:
                raise TypeError
            if value < 0:
                raise ValueError
            self.__width = value
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if type(value) != int:
                raise TypeError
            if value < 0:
                raise ValueError
            self.__height = value
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")
