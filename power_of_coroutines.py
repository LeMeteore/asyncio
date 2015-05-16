#!/usr/bin/env python
# -*- coding: utf-8 -*-

def menu():
    yield "spam"
    yield "eggs"
    yield "bacon"

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
        print("done")
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
        print("done")
        break
else:
    print(elt)


# how to send data to the generator

gen = receiver()
next(gen)
gen.send("hello world")
gen.send("hello world again")
