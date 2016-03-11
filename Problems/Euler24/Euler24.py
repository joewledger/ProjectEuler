#Project Euler Problem N
#Description

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import operator

num_digits = 10
desired_permutation = 1000000

sorted_digits = [x for x in xrange(0,num_digits)]
num_flips = desired_permutation - 1
lexicographic_digits = []
factorial = lambda n : reduce(operator.mul, [x for x in xrange(1, n+1)],1)

while(len(sorted_digits) > 0):
    f = factorial(len(sorted_digits) - 1)
    curr_digit_flips = int(num_flips / f)
    num_flips = num_flips % f
    lexicographic_digits.append(sorted_digits[curr_digit_flips])
    del sorted_digits[curr_digit_flips]
print("".join(str(x) for x in lexicographic_digits))
