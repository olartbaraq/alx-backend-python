#!/usr/bin/env python3
"""
text file to return an asyncio.Task function call
"""

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio.task object"""
    return asyncio.create_task(wait_random(max_delay))
