#!/usr/bin/env python3
"""
text file to loop coroutine 10 times and
yield a random number 0 to 10
asyncheonously
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    returns a generated num randomly after looping
    asynchronously

    """
    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
