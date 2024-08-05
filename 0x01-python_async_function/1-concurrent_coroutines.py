#!/usr/bin/env python3
'''run multiple wait_randoms at the same time'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''run n wait_randoms at the same time'''
    delays = [wait_random(max_delay) for _ in range(n)]
    delays = asyncio.as_completed(delays)
    return [await delay for delay in delays]
