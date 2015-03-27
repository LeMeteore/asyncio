#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import bs4

@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read_and_close()
    print(body)

#######

@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    return (yield from response.read_and_close())

def first_magnet(page):
    soup = bs4.BeautifulSoup(page)
    a = soup.find('a', title='Download this torrent using magnet')
    return a['href']


@asyncio.coroutine
def print_magnet(query):
    url = 'http://thepiratebay.se/search/{}/0/7/0'.format(query)
    page = yield from get(url, compress=True)
    magnet = first_magnet(page)
    print('{}: {}'.format(query, magnet))


if __name__ == '__main__':
    distros = ['archlinux', 'ubuntu', 'debian']
    loop = asyncio.get_event_loop()
    f = asyncio.wait([print_magnet(d) for d in distros])
    loop.run_until_complete(f)
