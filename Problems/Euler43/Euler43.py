#Project Euler Problem 43
#Description: Find the sum of all pandigital(0-9) numbers with the following property
#The substring of length 3 starting at digit n is evenly divisible by the (n-1)th prime for all substrings starting at digit 2

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

#Strategy: For each substring, pre-compute all possible combinations of digits.
#i.e. the substring starting at digit 2 must be divisible by 2 (as well as being pandigital).
#Therefore the allowed combinations are [012,014,016, ...,986]

import prime_utils
import integer_utils as i
import itertools
import operator

stream = prime_utils.Prime_Stream()
primes = stream.get_primes_under_n(stream[7])

#Creates a 3-level nested list in the following format
#[[[0,1,2],[0,1,4], ..., ], ... [[0,1,7], [0,3,4], ... , [9,8,6]]]
def calculate_len_three_substrings(primes):
    all_digits = {x for x in xrange(0,10)}
    three_permutations = [list(x) for x in itertools.permutations(all_digits,3)]
    return [[x for x in three_permutations if i.convert_digit_list_to_int(x) % y == 0] for index,y in enumerate(primes)]

prefix_tuple = lambda s : tuple(s[:2])
suffix_tuple = lambda s : tuple(s[1:])

substrings = calculate_len_three_substrings(primes)
prefix_map = {prefix_tuple(x) : x for x in substrings[-1]}

print(prefix_map)
