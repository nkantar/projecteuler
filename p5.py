#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

min = 10
min = 20

result = 0
number = min
divisors = 0
highest = 0

while not result:

    divisors = 0
    iterator = 1
    while iterator <= 20:

        if number % iterator == 0:
            divisors += 1
        else:
            break
        iterator += 1

    if divisors == min:
        result = number
        break

    if divisors > highest:
        highest = divisors

    if number % 10000000 == 0:
        print "Trying;", number
        print "Highest:", highest

    number += min

print result, "#winning"
