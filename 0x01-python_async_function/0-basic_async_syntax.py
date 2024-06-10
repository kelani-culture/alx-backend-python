#!/usr/bin/env python3

"""
wait random asyncio function doc
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    return a random float value between a specifc value
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
