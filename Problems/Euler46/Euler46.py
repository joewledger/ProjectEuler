#Project Euler Problem 46
#Description: Find the smallest odd composite that cannot be written as the sum of a prime and twice a square

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils
import math

def odd_composite_generator(prime_stream):
    n = 5
    while(True):
        if(not prime_stream.is_prime(n)):
            yield n
        n += 2

def is_sum_of_prime_and_twice_square(n,prime_stream):
    return any(prime_stream.is_prime(n - (x ** 2) * 2) for x in xrange(1,int(math.sqrt(n)) + 1))

prime_stream = prime_utils.Prime_Stream()
ocg = odd_composite_generator(prime_stream)
val = ocg.next()
while(is_sum_of_prime_and_twice_square(val,prime_stream)):
    val = ocg.next()
print(val)
    
