#!/usr/bin/python3
"""Square sinfini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Kvadrat obyektini inisializasiya edir.

        Args:
            size (int): Kvadratın ölçüsü (tərəfi).
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü əldə etmək üçün getter.

        Returns:
            int: Kvadratın ölçüsü.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin etmək üçün setter.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer (tam ədəd) deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın cari sahəsini qaytarır.

        Returns:
            int: Kvadratın sahəsi (size * size).
        """
        return self.__size ** 2
