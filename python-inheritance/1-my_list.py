#!/usr/bin/python3
"""MyList sinfini təyin edən modul."""


class MyList(list):
    """Standart list sinfindən miras alan sinif."""

    def print_sorted(self):
        """Siyahını artan sıra ilə çap edir (orijinalı dəyişmir)."""
        print(sorted(self))
