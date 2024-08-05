#!/usr/bin/env python3
'''asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.'''
import asyncio
import random


async def wait_random(max_delay=10):
  '''wait for a randome time between 0 and max_delay and return max_delay'''
  await asyncio.sleep(random.uniform(0, max_delay))
  return max_delay
