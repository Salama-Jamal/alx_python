#!/usr/bin/python3
"""Defines a class BaseGeometry based on 4-base_geometry.py"""


class BaseGeometry:
    """Class BaseGeometry.
    """
    def area(self):
        """Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate the input value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0: