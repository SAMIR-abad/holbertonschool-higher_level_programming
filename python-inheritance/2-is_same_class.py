#!/usr/bin/python3
"""Obyektin tipini yoxlayan modul."""


def is_same_class(obj, a_class):
    """Obyektin tam olaraq göstərilən sinfin instansiyası olub-olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        bool: Əgər tam eynidirsə True, əks halda False.
    """
    return type(obj) is a_class
