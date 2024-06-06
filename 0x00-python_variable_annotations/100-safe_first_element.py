#!/usr/bin/env python3
""" Module documentation for task 100 """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return None for empty list else return first element in list"""
    if lst:
        return lst[0]
    else:
        return None
