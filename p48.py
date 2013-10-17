#! /usr/bin/env python
from array import *
import itertools
import pprint
import math
import nik_math

max = 10
max = 1000

iterator = 1
sum = 0

while iterator <= max:
    sum += iterator**iterator
    iterator += 1

print "-----"
print str(sum)[-10:]
