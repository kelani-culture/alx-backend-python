#!/usr/bin/env python3
from collections.abc import Sequence
from typing import Iterable, List, Sequence, Tuple

"""
add type annotation to code
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return the element length
    """
    return [(i, len(i)) for i in lst]
