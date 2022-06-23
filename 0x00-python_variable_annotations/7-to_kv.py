#!/usr/bin/env python3

from typing import Tuple, Union
"""import type tuple from module typing for type annonation format"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple from arguments"""
    v = (v**2)
    return (k, v)
