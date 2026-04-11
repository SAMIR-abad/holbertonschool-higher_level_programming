#!/usr/bin/python3
"""list sinfindən miras alan MyList modulunu təyin edir."""


class MyList(list):
    """Standart list-ə əlavə funksionallıq verən sinif."""

    def print_sorted(self):
        """Siyahını artan sıra ilə çap edir, lakin orijinalı dəyişmir."""
        print(sorted(self))
