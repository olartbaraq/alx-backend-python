#!/usr/bin/env python3
from typing import Sequence, Iterable, Tuple, List
"""import from typing package necessary functions"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of iterables"""
    return [(i, len(i)) for i in lst]
