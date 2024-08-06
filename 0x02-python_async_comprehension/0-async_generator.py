#!/usr/bin/env python3
'''asynchronous coroutine that takes no arguments and returns a list of 10'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """Each time asynchronously waits 1 second,
        then yield a random number between 0 and 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
