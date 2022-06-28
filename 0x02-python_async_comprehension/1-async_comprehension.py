#!/usr/bin/env python3
"""
text file to return collected random
numbers ansynchronously
"""

from typing import List
import asyncio
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns 10 random numbers collected asynchronously
    from the imported function
    """
    result = [i async for i in async_generator()]
    return result
