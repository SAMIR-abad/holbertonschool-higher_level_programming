#!/usr/bin/python3
"""Rectangle-dan miras alan Square sinfi."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size):
        """Yeni bir Square yaradır.

        Args:
            size (int): Kvadratın tərəfi.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
