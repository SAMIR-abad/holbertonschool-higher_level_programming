#!/usr/bin/python3
"""Mirasalmanı yoxlayan modul."""


def inherits_from(obj, a_class):
    """Yalnız miras alınmış sinifləri yoxlayır."""
    return isinstance(obj, a_class) and type(obj) is not a_class
