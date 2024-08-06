#!/usr/bin/env python3
'''asynchronous coroutine that takes no arguments and returns a list of 10'''
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
