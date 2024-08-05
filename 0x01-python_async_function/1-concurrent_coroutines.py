#!/usr/bin/env python3
'''run multiple wait_randoms at the same time'''
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''run n wait_randoms at the same time'''
    delays = sorted([wait_random(max_delay) for _ in range(n)])
    return [await delay for delay in delays]
