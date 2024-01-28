"""
This base geometry class program have a validator
and it cares the self, name and value
"""

class BaseGeometry:
    """ This is the class for Base Geometry"""
    def __init__(self):
        """ This function is for initialization """ 
        pass 
    def area(self):
        """ This method is for the area of the base geometry with
            an exception
        """    
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ This is the integer validator of the method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
