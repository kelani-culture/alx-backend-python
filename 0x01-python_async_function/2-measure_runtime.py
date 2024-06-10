#!/usr/bin/env python3
"""
the measure time function documentation
"""

import asyncio
import time
from typing import Callable

wait_n: Callable[[int, int], list] = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    return total time for function execution
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    return (end - start) / n