#!/usr/bin/python3
"""BaseGeometry sinfini təyin edən modul."""


class BaseGeometry:
    """Həndəsə fiqurları üçün təməl sinif."""

    def area(self):
        """Hələlik tətbiq edilməmiş sahə metodu."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Tam ədədləri yoxlayan metod"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
