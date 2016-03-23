#Project Euler Problem 34
#Description: Find all the sum of all numbers that are equal to the sum of the factorials of their digits

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import operator
import integer_utils

factorial = {x : reduce(operator.mul, [y for y in xrange(1,x + 1)],1) for x in xrange(0,10)}
digit_factorial_equal = lambda n : n == sum(factorial[x] for x in integer_utils.convert_int_to_digit_list(n))

print(sum(e for e in xrange(10,factorial[9] * 7) if digit_factorial_equal(e)))
