#Project Euler Problem 21
#Find the sum of all amicable numbers under 10000
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which evenly divide into n).
#If d(a)=b and d(b)=a and a!=b, both a and b are amicable numbers

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils as p

util = p.Prime_Utils()
divisor_sum = lambda x : sum(util.get_divisor_list(x)[:-1])

amicable_numbers = []
d = {i : divisor_sum(i) for i in xrange(1,10000)}

for a in xrange(1,10000):
    b = d[a]
    if(b in d.keys()):
        if(d[b] == a and not b == a):
            amicable_numbers.append(a)
    else:
        value = divisor_sum(b)
        d[b] = value
        if(value == a):
            amicable_numbers.append(a)

print(sum(amicable_numbers))
