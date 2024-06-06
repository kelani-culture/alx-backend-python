#!/usr/bin/env python3
from typing import Any, Optional, Sequence, Union, NewType, TypeAlias

"""
Augmented the following code with the correct duck-typed annotations
"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    return None or a list
    """
    if lst:
        return lst[0]
    else:
        return None
