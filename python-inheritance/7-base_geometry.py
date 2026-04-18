#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul."""


class BaseGeometry:
    """Həndəsə fiqurları üçün baza sinfi."""

    def area(self):
        """Hələlik tətbiq edilməmiş sahə metodu."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd və müsbət olmasını yoxlayır."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
