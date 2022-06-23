#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Mapping, Any, Union, TypeVar
"""necessary import for arguments and return values"""

T = TypeVar('T')
"""Decorator functions can be expressed via generics"""


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]
                     ) -> Union[Any, T]:
    """return type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
