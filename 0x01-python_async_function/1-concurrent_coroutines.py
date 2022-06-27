#!/usr/bin/env python3
"""
test file to execute multiple coroutines at the
same time with async
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all delays value"""
    delay_list = []
    delay_count = []

    for spawn in range(n):
        """calls the number of times wait_random spawns"""
        delay_count.append(wait_random(max_delay))
    for delay_times_as_finished in asyncio.as_completed(delay_count):
        """loops through the array to push delay values as finished"""
        delays = await delay_times_as_finished
        delay_list.append(delays)

    return delay_list
