#Project Euler Problem 41
#Description: Find the largest n-digit pandigital prime
#n-digit pandigital: makes use of all digits 1 to n exactly once

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils
import integer_utils
import itertools

n_pandigital_permutations = lambda n : [y for y in itertools.permutations([x for x in xrange(1,n+1)])]

prime_stream = prime_utils.Prime_Stream()
all_pandigital_permutations = list(reversed([integer_utils.convert_digit_list_to_int(p) 
                                             for p in itertools.chain.from_iterable(n_pandigital_permutations(n) for n in xrange(1,10))]))
print(next(x for x in all_pandigital_permutations if prime_stream.is_prime(x)))
