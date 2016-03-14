#Project Euler Problem 32
#Description: Find the sum of all numbers that can be expressed as a 1-9 pandigital product

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils as p

def get_digit_list(n):
    digits = []
    while(n > 0):
        digits.append(n % 10)
        n /= 10
    return digits

def has_repeat_digits(n):
    digits = get_digit_list(n)
    return not len(digits) == len(set(digits))

def has_repeat_digits_list(integer_list):
    flatten = lambda l : sum(l,[])
    digit_lists = [get_digit_list(n) for n in integer_list]
    return not sum(len(l) for l in digit_lists) == len(set(flatten(digit_lists)))

def is_pandigital_product(n,prime_utils):
    contains_zero = lambda integer_list : any("0" in str(x) for x in integer_list)
    if has_repeat_digits(n): return False
    divisors = prime_utils.get_divisor_list(n)
    prod_multiplicands = [[n,d,n/d] for d in divisors]
    digit_length = lambda pm : sum(len(get_digit_list(l)) for l in pm)
    #for pm in prod_multiplicands:
    #    if(not (has_repeat_digits_list(pm) or contains_zero(pm) or digit_length(pm) < 9)):
    #        print(pm)
    #        return True
    #return False
    return any(not (has_repeat_digits_list(x) or contains_zero(x) or digit_length(x) < 9) for x in prod_multiplicands)

utils = p.Prime_Utils()
#for i in xrange(1000,10000):
#    is_pandigital_product(i,utils)



print(sum(i for i in xrange(1000,10000) if is_pandigital_product(i,utils)))
