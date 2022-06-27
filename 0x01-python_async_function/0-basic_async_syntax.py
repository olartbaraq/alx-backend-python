#!/usr/bin/env python3
"""The basics of async function,
also imports necessary packages
"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """returns the awaited response """
    time_delay = uniform(0, max_delay)
    await_resp = await asyncio.sleep(time_delay)
    return time_delay
