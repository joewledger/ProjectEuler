#Project Euler Problem 26
#Description: Find the fraction 1 / d for d < 1000 that contains the longest recurring cycle in its decimal fraction part

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils
import itertools

def get_length_longest_repeating_pattern(denominator):
    remainder = 10
    seen = {}
    for i in itertools.count(0):
        if remainder == 0:
            return 0
        elif remainder in seen:
            return i - seen[remainder]
        seen[remainder] = i
        remainder = 10 * (remainder % denominator)    

ps = prime_utils.Prime_Stream()
pattern_lengths = [get_length_longest_repeating_pattern(x) for x in ps.get_primes_under_n(1000)]
print(ps[pattern_lengths.index(max(pattern_lengths))])
