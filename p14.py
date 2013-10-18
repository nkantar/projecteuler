#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

number = 13
number = 999999

result = 0
counter_high = 0
number_high = 0
counter = 0

def is_valid(number, counter):
    if number == int(number):
        if number == 1:
            counter += 1
            return counter
        elif number % 2 == 0:
            counter += 1
            return is_valid(number / 2, counter)
        else:
            counter += 1
            return is_valid(3 * number + 1, counter)
    else:
        return 0

while number >= 1:
    count = is_valid(number, 0)
    if count > counter_high:
        counter_high = count
        number_high = number
    number -= 1

print "Number:", number_high
print "Count:", counter_high
