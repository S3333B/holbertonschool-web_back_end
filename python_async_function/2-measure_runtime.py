#!/usr/bin/env python3
"""
This module measures the runtime of wait_n.
"""

import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of wait_n and return
    the average time per coroutine.

    Args:
        n: Number of coroutines.
        max_delay: Maximum delay.

    Returns:
        The average execution time.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - start_time

    return total_time / n
