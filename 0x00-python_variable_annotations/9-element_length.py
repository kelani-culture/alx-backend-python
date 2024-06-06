#!/usr/bin/env python3
"""
add type annotation to code
"""
from collections.abc import Sequence
from typing import Iterable, List, Sequence, Tuple



def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return the element length
    """
    return [(i, len(i)) for i in lst]
