#! /usr/bin/env python
from array import *

total = 0
number = 2

def add_divisors(number):
	index = 1
	total = 0
	while index <= (number / 2):
		if number % index == 0:
			total = total + index
		index = index + 1
	return total

while number < 10000:
	if number == add_divisors(add_divisors(number)):
		if number != add_divisors(number):
			total = total + number + add_divisors(number)
	number = number + 1

print total / 2