#!/usr/bin/env python3
'''asynchronous coroutine that takes no arguments and returns a list of 10'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects async generated list and return it"""
    return [_ async for _ in async_generator()]
