#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import Sequence, Iterable, Tuple, List
"""import from typing package necessary functions"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of iterables"""
    return [(i, len(i)) for i in lst]
