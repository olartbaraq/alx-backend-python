#!/usr/bin/env python3

import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """returns 10 random numbers collected asynchronously
    from the imported function
    """
    result = [i async for i in async_generator()]
    return result
