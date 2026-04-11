#!/usr/bin/python3
"""Obyektin atributlarını axtaran modul."""


def lookup(obj):
    """Obyektin mövcud atribut və metodlarının siyahısını qaytarır.

    Args:
        obj: Yoxlanılacaq obyekt.

    Returns:
        list: Atribut və metod adlarının siyahısı.
    """
    return dir(obj)
