#!/usr/bin/python3
"""Module defining the Base class."""

class Base:
    """The Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int): If provided, assign it to the public instance attribute id.
                      Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects