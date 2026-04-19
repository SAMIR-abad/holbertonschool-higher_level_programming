#!/usr/bin/python3
"""a"""


class BaseGeometry:
    """A"""

    def area(self):
        """AAAAAAAAAA"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """AAAAAAA"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
