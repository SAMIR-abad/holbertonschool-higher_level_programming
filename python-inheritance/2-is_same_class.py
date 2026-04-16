#!/usr/bin/python3
"""Obyektin tipini yoxlayan modul."""

def is_same_class(obj, a_class):
    """Obyektin tam olaraq göstərilən sinfin instansiyası olub-olmadığını yoxlayır."""
    return type(obj) is a_class
