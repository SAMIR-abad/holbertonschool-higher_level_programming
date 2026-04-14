#!/usr/bin/python3
"""izah."""


class MyList(list):
    """izah"""

    def __init__(self, *args):
        """izah"""

        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args))
            )
        super().__init__(*args)

    def print_sorted(self):
        """izah"""

        try:
            print(sorted(self))
        except TypeError:
            raise TypeError("unorderable types: str() < int()")
