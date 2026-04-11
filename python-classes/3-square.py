#!/usr/bin/python3
"""Kvadrat sinfini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Kvadrat obyektini inisializasiya edir.

        Args:
            size (int): Kvadratın ölçüsü (tərəfi). Standart dəyəri 0-dır.

        Raises:
            TypeError: Əgər size integer (tam ədəd) deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın cari sahəsini qaytarır.

        Returns:
            int: Kvadratın sahəsi (size * size).
        """
        return self.__size ** 2
