"""
a python file for question no. 5
"""
class BaseGeometry():
    """
    a class
    """
    def area(self):
        """
        Public instance method, that raises an Exception with the message: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method, that validates value.
        you can assume name is always a string
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
