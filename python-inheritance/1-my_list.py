#!/usr/bin/python3
"""
This module contains the MyList class.
"""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        Assumes all elements in the list are integers.
        """
        print(sorted(self))
