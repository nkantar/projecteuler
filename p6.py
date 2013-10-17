#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

max = 10
max = 100

sum_of_squares = 0

sum = 0
square_of_sum = 0

iterator = 1
while iterator <= max:
    sum_of_squares += iterator ** 2
    sum += iterator
    iterator += 1

square_of_sum = sum ** 2

print sum_of_squares, square_of_sum, int(math.fabs(sum_of_squares - square_of_sum))
