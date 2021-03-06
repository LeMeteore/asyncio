#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio as aio
import websockets

@aio.coroutine
def hello(ws, uri):
    # websocket.recv is a coroutine
    # to execute a coroutine, use yield from
    name = yield from ws.recv()
    print("< {}".format(name))
    greeting = "hello {}!".format(name)
    # hello is a coroutine
    # it should contains at - 1 yield from expression
    yield from ws.send(greeting)
    print("> {}".format(greeting))


@aio.coroutine
def handler(ws, uri):
    # best way to handle connections
    while True:
        n = yield from ws.recv()
        if n is None:
            break
        print("< {}".format(n))
        greeting = "hello {}".format(n)
        yield from ws.send(greeting)
        print("> {}".format(greeting))


start_server = websockets.serve(handler,
                                'localhost',
                                8765)
aio.get_event_loop().run_until_complete(start_server)
aio.get_event_loop().run_forever()
