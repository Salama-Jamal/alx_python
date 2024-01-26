#!/usr/bin/python3
"""
Module 4-base_geometry
Defines the BaseGeometry class with an area method.
"""

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

if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(dir(bg)[:-1])  # Exclude the last element to match the expected output
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

