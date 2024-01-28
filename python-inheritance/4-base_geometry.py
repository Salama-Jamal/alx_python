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
