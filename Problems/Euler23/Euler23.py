#Project Euler Problem 23
#Find the sum of all numbers that cant be expressed as the sum of two abundant numbers
#Abundant numbers: numbers for which the sum of their proper divisors is greater than the number itself

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

from itertools import combinations as combination
import prime_utils as p
import combinatorics_utils as c_utils
util = p.Prime_Utils()

threshold = 28134

proper_divisor_sum = lambda n : sum(util.get_divisor_list(n)[:-1])
abundant_numbers = [x for x in xrange(1,threshold) if x < proper_divisor_sum(x)]
abundant_set = set(abundant_numbers)

def is_abundant_sum(n,abundant_numbers):
    i = 0
    while(abundant_numbers[i] <= n / 2):
        if(n - abundant_numbers[i] in abundant_set):
            return True
        i += 1
    return False

print(sum(x for x in xrange(1,threshold) if not is_abundant_sum(x,abundant_numbers)))
