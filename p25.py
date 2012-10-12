#! /usr/bin/env python

fib1 = 1
fib2 = 1
temp = 0
counter = 2

while len(str(fib2)) < 1000:
	temp = fib2
	fib2 = fib2 + fib1
	fib1 = temp
	counter = counter + 1

print counter