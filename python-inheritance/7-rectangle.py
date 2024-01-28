
"""
BaseGeometry class with a public instance method area().
"""
class MetaClass(type):
    """
    Oeveride dir() method to exclude __init__subclass__
    """
    def __dir__(cls):
        return[attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=MetaClass):
    """
    BaseGeometry class with a public instance method area().
    """
    def __dir__(cls):
        return[attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    def area(self):
        """
        Public instance method that raises an Exception with the message
        "area() is not implemented".
        """
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates an integer value.
        Raises a TypeError if the value is not an integer.
        Raises a ValueError if the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <=0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
         
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """
        Public instance method that calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of the rectangle in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
