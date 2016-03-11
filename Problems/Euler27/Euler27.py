#Project Euler Problem 27
#Find the quadratic expression of the form n^2 + an + b which produces the most consecutive primes for n in (0,1,...).
#In addition a and b must both be in the range (-1000,1000)
#Then return a * b

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import prime_utils as p

ps = p.Prime_Stream()

def get_num_primes_generated(a,b,prime_stream):
    n = 0
    while(prime_stream.is_prime(n ** 2 + a * n + b)):
        n += 1
    return n

max_v,max_a,max_b = 0,0,0

for b in ps.get_primes_under_n(1000):
    for a in xrange(1 - b, 1000):
        pg = get_num_primes_generated(a,b,ps)
        if(pg > max_v):
            max_v,max_a,max_b = pg,a,b
print(max_a * max_b)
