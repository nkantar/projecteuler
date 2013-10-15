#! /usr/bin/env python

import math

def is_prime(number):

    ############
    # exceptions

    # negative, 0, 1, even
    if number < 2 or (number % 2 == 0 and number != 2):
        return False

    # 2
    if number == 2:
        return True

    ###########
    # iteration

    divisor = 3
    root = int(math.sqrt(number))

    while divisor <= root:
        if number % divisor == 0:
            return False

        divisor += 2

    return True
