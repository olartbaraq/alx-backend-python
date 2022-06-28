#!/usr/bin/env python3
"""
text file to execute imported function 4 times
in parallel to asyncio.gather
"""
from typing import List
import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the total runtime to run async_comprehension
    four times using asyncio.gather
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop = time.perf_counter()
    return stop - start
