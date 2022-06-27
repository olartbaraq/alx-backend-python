#!/usr/bin/env python3
"""
text file to measure the total execution time
"""

import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns the total execution time"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    return (end - start) / n
