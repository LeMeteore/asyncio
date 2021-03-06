#!/usr/bin/env python
# -*- coding: utf-8 -*-


from itertools import count, islice
from math import sqrt
from functools import reduce
from collections import Counter


""" Un nombre premier est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs (qui sont alors 1 et lui-même). Ainsi, 1 n'est pas premier car il n'a qu'un seul diviseur entier positif ; 0 non plus car il est divisible par tous les entiers positifs.'
"""

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

def primes_generator(n=100):
    for i in range(2, n):
        if is_prime(i):
            yield i
            i += 1

def primes_generator2():
    f = sieve()
    yield from f


"""un nombre composé est le produit d'au moins 2 nombres premiers (qu'ils soient distincts ou identiques)."""

# not prime? so it is a composite number
def composites_generator(n=100):
    for i in range(2,n):
        if not is_prime(i):
            yield (i, primes_factors(i))


# returns a list of prime factors
def primes_factors(n=100):
    f = list()
    d = 2;
    if is_prime(n): return [1, n]
    while (n>1):
        while n%d==0:
            f.append(d)
            n/=d
        d+=1
    return f

# returns factors & number of time they appears
def primes_factors2(n=100):
    f = list()
    ff = list()
    d = 2;
    if is_prime(n): return [1, n]
    while (n>1):
        while n%d==0:
            f.append(d)
            n/=d
        d+=1
    # ff is a list of tuples (factor, time)
    for i in Counter(f).items():
        ff.append(i)
    return ff

def primes_factors_generator(n=100):
    f = list()
    d = 2;
    if is_prime(n): return [1, n]
    while (n>1):
        while n%d==0:
            yield d
            n/=d
        d+=1


"""a divise b si b = k.a avec k appartenant a Z """

def divisors(n=100):
    d = list()
    for i in range(2, int(n/2+1)):
        if n%i == 0: d.append(i)
    return d

def divisors_generator(n=100):
    for i in range(1, int(n/2+1)):
        if n%i == 0: yield i
    # n is a divisor of n
    yield n

def divisors_generator1(n=100):
    for d in iter(divisors(n)): yield d

def divisorGen(n=100):
    #factors = list(primes_factors_generator(n))
    factors = primes_factors2(n)
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

###

def is_divisor(a, b):
    divide = False
    if a in divisors(b):
        divide = True
    return (divide, divisors(b))

def is_prime_divisor(a, b):
    divide = False
    if a in primes_factors(b):
        divide = True
    return (divide, primes_factors(b))
