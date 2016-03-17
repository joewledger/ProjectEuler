#Project Euler Problem 40
#Description:

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import integer_utils
import operator

i = 0
digits = []
while(len(digits) < 1000000):
    i += 1
    digits.extend(integer_utils.convert_int_to_digit_list(i))

print(reduce(operator.mul,[digits[10 ** j - 1] for j in xrange(0,7)],1))
