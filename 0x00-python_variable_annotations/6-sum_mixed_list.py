#!/usr/bin/env python3
from typing import List, Union
""" imports annotated type list from module typing"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of int and float from list"""
    sum = 0
    for num in mxd_lst:
        sum += float(num)
    return sum
