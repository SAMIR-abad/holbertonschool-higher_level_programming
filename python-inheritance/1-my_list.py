#!/usr/bin/python3
"""MyList modulu"""


class MyList(list):
    """list sinfindən miras alan MyList sinfi"""

    def print_sorted(self):
        """Siyahını artan sıra ilə çap edir"""
        print(sorted(self))
