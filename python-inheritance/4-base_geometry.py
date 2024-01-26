#!/usr/bin/python3

class BaseGeometry:
    """
    A class representing a base geometry.

    Methods:
    - area(self): Raises an Exception with the message "area() is not implemented".
    """
    def area(self):
        """
        Calculate the area. This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()
print(dir(bg))





