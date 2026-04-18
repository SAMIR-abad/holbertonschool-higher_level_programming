#!/usr/bin/python3
"""BaseGeometry modulu."""


class BaseGeometry:
    """Həndəsə üçün baza sinfi."""

    def area(self):
        """Hələlik tətbiq edilməyib."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd və 0-dan böyük olmasını yoxlayır.
        
        Qeyd: type() istifadə edirik, çünki isinstance(True, int) True qaytarır,
        amma biz boolean-ları qəbul etməməliyik.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
