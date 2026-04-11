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
        """Kvadratın ölçüsünü əldə etmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın cari sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' simvolları ilə standart çıxışa çap edir.
        
        Əgər ölçü (size) 0-a bərabərdirsə, sadəcə boş bir sətir çap edir.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
