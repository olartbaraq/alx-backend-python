#!/usr/bin/env python3
from typing import Callable
""" imports annotated type list from module typing"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to return a function using argument as parameter"""
    def return_multiplier(num: float) -> float:
        """ Callback function for make_multiplier"""
        return num * multiplier
    return(return_multiplier)
