#!/usr/bin/env python3
"""
async comprehension for returing a list
"""
import asyncio
from typing import List, Callable

async_generator: Callable = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    return [ i async for i in async_generator() ]