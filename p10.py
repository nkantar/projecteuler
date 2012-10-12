#! /usr/bin/env python
from array import *

total = 10
primes = array('i',[2,3,5])
num = 7

def is_prime(num, index):
	while index < len(primes):		
		if num % primes[index] == 0:
			return False
		else:
			index = index + 1
	return True

while num < 2000000:
	if is_prime(num,0):
		primes.append(num)
		total = total + num
	num = num + 2

print total