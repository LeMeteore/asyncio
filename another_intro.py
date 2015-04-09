#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

@asyncio.coroutine
def my_coroutine(task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))
    # sleep: Coroutine that completes after a given time in sec.
    # during sleeping, another task will be launched
    yield from asyncio.sleep(seconds_to_sleep)
    print('{0} is finished'.format(task_name))

tasks = [
    # async: wrap coroutine in a future
    asyncio.async(my_coroutine('task1', 4)),
    # Task: a coroutine wrapped in a Future
    asyncio.Task(my_coroutine('task2', 3)),
    asyncio.Task(my_coroutine('task3', 2))
]

def run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        # wait: return a future aggregating results from given coroutines/futures
        asyncio.wait(tasks)
        )
    loop.close()

if __name__ == '__main__':
    run()
