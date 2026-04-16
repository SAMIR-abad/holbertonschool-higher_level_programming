#!/usr/bin/python3
"""BaseGeometry-dən miras alan Rectangle sinfi."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Düzbucaqlı təmsil edən sinif."""

    def __init__(self, width, height):
        """Yeni bir Rectangle yaradır və dəyərləri yoxlayır."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Düzbucaqlının sahəsini hesablayır və qaytarır."""
        return self.__width * self.__height

    def __str__(self):
        """Düzbucaqlı haqqında məlumatı formatlı şəkildə qaytarır."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
