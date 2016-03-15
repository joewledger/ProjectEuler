#Project Euler Problem 35
#Description: Find the number of circular primes under one million
#A circular prime is defined as a prime for which all rotations of its digits are also prime

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils
import integer_utils

def get_digit_rotations(n):
    digit_list = integer_utils.convert_int_to_digit_list(n)
    rotations = []
    for i in xrange(0,len(digit_list)):
        curr_number = digit_list[i:]
        curr_number.extend(digit_list[:i])
        rotations.append(integer_utils.convert_digit_list_to_int(curr_number))
    return rotations

def is_circular_prime(n,prime_stream):
    rotations = get_digit_rotations(n)
    return all(prime_stream.is_prime(rotation) for rotation in rotations)

prime_stream = prime_utils.Prime_Stream()
primes = prime_stream.get_primes_under_n(1000000)
print(sum(1 for i in primes if is_circular_prime(i,prime_stream)))
