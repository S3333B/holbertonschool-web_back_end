#!/usr/bin/env python3
"""
This module defines a coroutine that executes multiple
wait_random coroutines concurrently.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the given max_delay and
    return the delays in ascending order.

    Args:
        n: Number of coroutines to spawn.
        max_delay: Maximum delay for each coroutine.

    Returns:
        A list of delays in ascending order.
    """
    delays = []

    tasks = [asyncio.create_task(wait_random(max_delay))
             for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
