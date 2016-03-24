#Project Euler Problem 92
#Description: A number chain is created by continuously adding the square of the digits to form a new number until it has been seen before
#How many starting numbers under 10 million will arrive at 89



import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import integer_utils

next = lambda n : sum(x ** 2 for x in integer_utils.convert_int_to_digit_list(n))

max_number = 10000000
cache = {1 : 1, 89 : 89}

max_next = 9 ** 2 * len(integer_utils.convert_int_to_digit_list(max_number - 1))
for i in xrange(1,max_next + 1):
    numbers = [i]
    while(not numbers[-1] in cache):
        numbers.append(next(numbers[-1]))
    end_value = cache[numbers[-1]]
    for x in numbers:
        cache[x] = end_value

print(sum(1 for x in xrange(1,max_number) if cache[next(x)] == 89))
