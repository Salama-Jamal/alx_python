#!/usr/bin/python3
""" this module contains class BaseGeometry """


class BaseGeometry:
    """ defines the class BaseGeometry """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ validates the given value is a positive integer """
        
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
