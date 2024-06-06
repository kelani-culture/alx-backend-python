#!/usr/bin/env python3
from typing import Tuple, Union
from math import e
"""
return a tuple of key and value pair
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a tuple of values
    """
    return (k, float(v ** 2))
