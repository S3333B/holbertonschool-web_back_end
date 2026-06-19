#!/usr/bin/env python3
"""
This module defines a coroutine that executes multiple
tasks concurrently and returns their delays.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return the delays
    in ascending order.

    Args:
        n: Number of tasks to create.
        max_delay: Maximum delay.

    Returns:
        A list of delays in ascending order.
    """
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
