#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio as aio

def hello_world(loop):
    print('hello world')
    # stop the loop after printing the msg
    loop.stop()

# get the current loop
loop = aio.get_event_loop()
# run hello_world function as soon as possible
loop.call_soon(hello_world, loop)

# run loop forever
loop.run_forever()
# close the loop that has been stopped inside hello_world
loop.close()
