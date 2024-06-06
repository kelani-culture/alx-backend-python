#!/usr/bin/env python3
"""
return a tuple of key and value pair
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a tuple of values
    """
    return (k, float(v**2))
