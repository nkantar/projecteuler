#! /usr/bin/env python
from array import *

primes = array('i',[2,3,5,7,11])
num = 13

def is_prime(num, index):
	while index < len(primes):		
		if num % primes[index] == 0:
			return False
		else:
			index = index + 1
	return True

while len(primes) < 10001:
	if is_prime(num,0):
		primes.append(num)
	num = num + 2

print primes[len(primes)-1]