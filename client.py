#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio as aio
import websockets

@aio.coroutine
def hello():
    # retrieve ws url
    ws = yield from websockets.connect('ws://localhost:8765')
    # get the name that will be sent
    name = input("what's your name? ")
    # hello is a coroutine,
    # it should have one yield from expression
    yield from ws.send(name)
    print("> {}".format(name))
    # ws.recv() is a coroutine
    # to execute it, use yield from expression
    greeting = yield from ws.recv()
    print("< {}".format(greeting))

# get the current loop and run hello
aio.get_event_loop().run_until_complete(hello())
