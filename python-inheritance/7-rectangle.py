#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-rectangle.py"""



BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


    def area(self):
        """Area Function
        Return height multiply by width
        """
        return self.__height * self.__width
    

    def __str__(self):
        """__str__ Function
        Return [Rectangle] <width>/<height>
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)