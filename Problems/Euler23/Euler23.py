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
all_linear_combinations = {}

proper_divisor_sum = lambda n : sum(util.get_divisor_list(n)[:-1])
abundant_numbers = [x for x in xrange(1,threshold) if x < proper_divisor_sum(x)]

pn = util.get_perfect_numbers()
perfect_numbers = [pn.next()]
while(perfect_numbers[-1] < threshold):
    perfect_numbers.append(pn.next())
perfect_numbers = perfect_numbers[:-1]

naturally_abundant = []
for x in abundant_numbers:
    if(not any(x % y == 0 for y in naturally_abundant) and not any(x % y == 0 for y in perfect_numbers)):
        naturally_abundant.append(x)

print(len(abundant_numbers))
print(naturally_abundant)
