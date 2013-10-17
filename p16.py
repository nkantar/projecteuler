#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

max = 15
max = 1000

sum = 0

digits = str(2**max)

for digit in digits:
    sum += int(digit)

print sum
