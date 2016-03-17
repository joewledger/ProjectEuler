#Project Euler Problem 37
#Description: Find the sum of the 11 primes that are truncatable from the both directions
#A prime is truncatable from left to right if recursively removing its first digit still yields a prime at each step
#I.e. 3797 -> 797,97,7 which are all prime

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils
import integer_utils

def is_truncatable(n,prime_stream):
    prime_digit_list = lambda d : prime_stream.is_prime(integer_utils.convert_digit_list_to_int(d))
    truncate_left = lambda d : all(prime_digit_list(d[x:]) for x in xrange(0,len(d)))
    truncate_right = lambda d : all(prime_digit_list(d[:x]) for x in xrange(1,len(d)))

    digit_list = integer_utils.convert_int_to_digit_list(n)
    return truncate_left(digit_list) and truncate_right(digit_list)

def truncatable_prime_generator(prime_stream):
    i = 5
    while(True):
        value = prime_stream[i]
        if(is_truncatable(value,prime_stream)):
            yield value
        i += 1

prime_stream = prime_utils.Prime_Stream()
tpg = truncatable_prime_generator(prime_stream)

print(sum(tpg.next() for x in xrange(0,11)))
