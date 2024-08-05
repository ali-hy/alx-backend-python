#!/usr/bin/env python3
'''measure the runtime of the function fomr wait_n'''
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''run n wait_randoms at the same time'''
    delays = [task_wait_random(max_delay) for _ in range(n)]
    delays = asyncio.as_completed(delays)
    return [await delay for delay in delays]
