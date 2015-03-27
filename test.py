#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiohttp
import asyncio

@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read_and_close()
    print(body)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_page('http://example.com'))
