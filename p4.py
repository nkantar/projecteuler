#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

a = 999
highest = 0

while a > 99:
    b = 999
    while b > 99:
        product = a * b
        if nik_math.is_palindromic(product) and product > highest:
            highest = product
        b -= 1
    a -= 1

print highest
