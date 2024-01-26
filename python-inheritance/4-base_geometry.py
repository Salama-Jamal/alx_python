#!/usr/bin/python3

from base_geometry import BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

#!/usr/bin/python3

BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# 4-base_geometry.py

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
