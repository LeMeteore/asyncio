#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
 
@asyncio.coroutine
def my_coroutine(seconds_to_sleep=3):
    print('my_coroutine sleeping for: {0} seconds'.format(seconds_to_sleep))
    yield from asyncio.sleep(seconds_to_sleep)
 
 
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(asyncio.Task(my_coroutine()))
)
loop.close()

