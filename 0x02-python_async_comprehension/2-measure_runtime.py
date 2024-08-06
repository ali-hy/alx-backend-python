#!/usr/bin/env python3
"""Mesures time taken by 4 async_comprehension executions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the time taken to run four concurrent async_comprehension
    calls and returns the total time taken"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
