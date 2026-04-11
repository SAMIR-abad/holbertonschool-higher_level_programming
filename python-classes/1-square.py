#!/usr/bin/python3
"""Kvadrat sinfini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size):
        """Kvadrat obyektini inisializasiya edir.

        Args:
            size: Kvadratın ölçüsü (tərəfi).
        """
        self.__size = size
