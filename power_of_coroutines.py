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
