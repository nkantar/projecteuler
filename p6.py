#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

total = 12
total = 1000

num_max = 5
num_max = 998 # since a, b, and c must be at least 1 each, and the total is 1000

a = 1

while a <= total - 2:
    b = 1
    while b <= total - (a + 1):
        c = 1
        while c <= total - (a + b):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == total:
                print a * b * c
                raise SystemExit, "#winning" # not very Pythonic, I admit
            c += 1
        b += 1
    a += 1
