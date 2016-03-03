#Project Euler Problem 5
#Finds the smallest number evenly divisible by each of the numbers 1-20

import time
from operator import mul
import Prime_Generator as p_gen
time.clock()

primes = p_gen.generate_primes(20,sieve="eratosthenes")
prod_primes = reduce(mul,primes,1)
value = prod_primes
while(not all(value % x == 0 for x in xrange(1,21))):
	value += prod_primes
print("Answer: %s" % value)
print("Calculation took %s seconds" % str(time.clock()))