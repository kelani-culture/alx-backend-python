#!/usr/bin/env python3
from typing import Callable

"""
A function that returns a function multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function multiplier
    """
    return lambda x: x * multiplier
