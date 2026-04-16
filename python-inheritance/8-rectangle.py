#!/usr/bin/python3
"""BaseGeometry-dən miras alan Rectangle sinfi."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Düzbucaqlı təmsil edən sinif."""

    def __init__(self, width, height):
        """Yeni bir Rectangle instansiyası yaradır.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
