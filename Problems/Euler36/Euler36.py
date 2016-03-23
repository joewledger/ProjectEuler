#Project Euler Problem 36
#Description: Find the sum of all numbers less than one million that are palindromic in base 2 and base 10

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import integer_utils

is_palindrome = lambda digit_list : digit_list == list(reversed(digit_list))
binary_palindrome = lambda x : is_palindrome(integer_utils.int_to_binary_digit_list(x))

def odd_palindrome_generator():
    for x in xrange(0,499999):
        n = x * 2 + 1
        digits = integer_utils.convert_int_to_digit_list(n)
        if(is_palindrome(digits)):
            yield n
#print([x for x in odd_palindrome_generator()][-100:])
print(sum(x for x in odd_palindrome_generator() if binary_palindrome(x)))
