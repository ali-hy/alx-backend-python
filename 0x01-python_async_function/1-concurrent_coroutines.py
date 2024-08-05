#!/usr/bin/env python3
'''run multiple wait_randoms at the same time'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> float:
    '''run multiple wait_randoms at the same time'''
    delays = [wait_random(max_delay) for i in range(n)]
    return asyncio.gather(*delays)