#!/usr/bin/env python
# -*- coding: utf-8 -*-

def menu():
    yield "spam"
    yield "eggs"
    yield "bacon"
    yield "\n"

# a simple generator
gen = menu()
print(type(gen))

# iteration over a generator
for elt in gen:
    print(elt)


# another example

def count():
    i = 0
    # no problem even with an infinite loop
    while True:
        print("tick")
        i += 1
        yield i

gen = count()

# because of the while loop, let's break after 20 iterations
for elt in gen:
    if elt == 20:
        print("done\n")
        break
else:
    print(elt)


# we can "send" the data to be yielded

def receiver():
    print("ready")
    while True:
        data = yield
        print("received {!r}".format(data))

gen = receiver()
print(type(gen))

# because of the while loop, let's break after 20 iterations
a = 20
for elt in gen:
    a -= 1
    if a == 0:
        print("done\n")
        break
else:
    print(elt)


# how to send data to the generator

gen = receiver()
next(gen)
gen.send("hello world")
gen.send("hello world again")

# yield est bel et bien un mécanisme de coroutines,
# c'est-à-dire un point de suspension dans l'exécution d'une fonction,
# que l'on peut utiliser pour échanger des données avec elle.


# let's create a decorator that will 'start' the generator for us
# you should always call next one time before being able to use
# your newly created generator

def coroutine(func):
    def starter(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return starter

# let's create a printer who print whatever sent to him
@coroutine
def printer(prefix=''):
    while True:
        data = yield
        print("{}{}".format(prefix, data))

gen = printer()

# sending some letters to our generator
for i in "coroutines are awesome and powerful\n":
    gen.send(i)


# let's create a grepper, who filter data the send it to a target
@coroutine
def grepper(pattern, target):
    while True:
        data = yield
        if pattern in data:
            target.send(data)


ptr = printer()
grep = grepper('python', ptr)

for i in ["python is nice", "bash is nice too", "same thing for rust", "but let's keep with python"]:
    grep.send(i)
