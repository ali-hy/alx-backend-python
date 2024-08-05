#!/usr/bin/env python3
'''measure the runtime of the function fomr wait_n'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure the runtime of the function fomr wait_n'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start)
