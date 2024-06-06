#!/usr/bin/env python3
"""
A function that returns a function multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function multiplier
    """
    return lambda x: x * multiplier
