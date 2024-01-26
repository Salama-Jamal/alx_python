#!/usr/bin/python3
"""Defines a class BaseGeometry based on 7-rectangle.py"""



Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)