#!/usr/bin/env python3
from typing import List
"""imported annotated List type"""


def sum_list(input_list: List[float]) -> float:
    """returns the sum of all elements in the list"""
    sum = 0
    for num in input_list:
        sum += num
    return sum
