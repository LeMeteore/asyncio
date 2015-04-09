#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

@asyncio.coroutine
def my_coroutine(future, task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))
    # sleep: Coroutine that completes after a given time in sec.
    # during sleeping, another task will be launched
    yield from asyncio.sleep(seconds_to_sleep)
    # set_result: mark the future done and set its result
    future.set_result('{0} is finished'.format(task_name))


# print the result kept by the future
def got_result(future):
    # result: return the result this future represent
    # can also be CancelledError, InvalidStateError, or an Exception if set
    print(future.result())

# an object that will contain something :)
future1 = asyncio.Future()
future2 = asyncio.Future()
future3 = asyncio.Future()

# Add a callback to be run when the future becomes done
future1.add_done_callback(got_result)
future2.add_done_callback(got_result)
future3.add_done_callback(got_result)

tasks = [
    # async: wrap coroutine in a future
    asyncio.async(my_coroutine(future1, 'task1', 4)),
    # Task: a coroutine wrapped in a Future
    asyncio.Task(my_coroutine(future2, 'task2', 3)),
    asyncio.Task(my_coroutine(future3, 'task3', 2))
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



# >>> @asyncio.coroutine
# ... def corou():
# ...   yield from asyncio.sleep(5)
# ...
# >>> f1 = asyncio.async(corou())
# >>> f2 = asyncio.Task(corou())
# >>> type(f1)
# <class 'asyncio.tasks.Task'>
# >>> type(f2)
# <class 'asyncio.tasks.Task'>
# >>> t = [f1, f2]
# >>> l = asyncio.get_event_loop()
# >>> l.run_until_complete(asyncio.wait(t))
# ({<Task finished coro=<corou() done, defined at <stdin>:1> result=None>, <Task finished coro=<corou() done, defined at <stdin>:1> result=None>}, set())
