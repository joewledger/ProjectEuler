#Project Euler Problem 20
#Description: Find the sum of the digits in the number 100!

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import operator
import integer_utils
factorial = reduce(operator.mul, [x for x in xrange(1,101)],1)

print(sum([x for x in integer_utils.convert_int_to_digit_list(factorial)]))
