#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

number = 1
minimum = 5
minimum = 500

divisors = 1
highest = 0
sum = 0 

while divisors <= minimum:
    # print "---"

    # generate triangular number to try
    sum += number

    # print "Trying:", sum
    # print "Number:", number

    # find all its divisors
    # note: incorrect for some (namely small) values
    divisor = 1
    divisors = 0
    while divisor <= int(math.sqrt(sum)):
        if sum % divisor == 0:
            divisors += 1
        divisor += 1

    divisors *= 2

    if divisors % (divisor - 1) == 0:
        divisors -= 1
    
    # find all its divisors
    # note: this shit is slooow
    # while divisor <= sum / 2:
    #     if sum % divisor == 0:
    #         divisors += 1
    #     divisor += 1
    # divisors += 1
    
    # keep track of highest, just for fun
    if divisors > highest:
        highest = divisors

    # print "Divisors:", divisors
    # print "Highest:", highest

    # increment iterator
    number += 1

print "-----"
print "#winning", sum
