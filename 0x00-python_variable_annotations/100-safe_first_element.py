#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import Sequence, Any, Union
"""necessary import to use functions"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns The types of the elements"""
    if lst:
        return lst[0]
    else:
        return None
