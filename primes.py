#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import count, islice
from math import sqrt

def is_prime(n):
    return all(n%i for i in range(2, n))

def is_prime2(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(n)))

def sieve(n=100):
    n1 = n + 1
    s = list(range(n1)) # leave off `list()` in Python 2
    # we know that 1 is not prime
    s[1] = 0
    # to check for prime, just check until sqrt(n)
    sqrtn = int(round(sqrt(n)))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # ???
            s[i*i: n1: i] = [0] * len(range(i*i, n1, i))
    # return all the non zero
    return filter(None, s)

def primes_generator():
    for i in range(2, 100):
        if is_prime(i):
            yield i
            i += 1

def primes_generator2():
    f = sieve()
    yield from f
