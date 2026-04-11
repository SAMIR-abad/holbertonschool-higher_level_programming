#!/usr/bin/python3
"""
Bu modul MyList sinfini təyin edir.
"""


class MyList(list):
    """
    Siyahı obyektindən miras alan və əlavə funksionallığı olan sinif.
    """

    def print_sorted(self):
        """
        Siyahıdakı tam ədədləri artan sıra ilə çap edir.
        """
        print(sorted(self))
