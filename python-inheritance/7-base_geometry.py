#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul."""


class BaseGeometry:
    """Həndəsə fiqurları üçün təməl sinif."""

    def area(self):
        """Sahəni hesablayır (hələlik tətbiq edilməyib)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Tam ədədləri yoxlayır"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
