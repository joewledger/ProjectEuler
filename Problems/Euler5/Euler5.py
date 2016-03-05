#Project Euler Problem 5
#Finds the smallest number evenly divisible by each of the numbers 1-20

from operator import mul
import sys
sys.path.append("../../Utils")
sys.path.append("Utils")
import prime_utils as p

stream = p.Prime_Stream()
primes_under_20 = stream.get_primes_under_n(20)
composites_under_20 = [x for x in xrange(1,21) if not x in primes_under_20]
prod_primes = reduce(mul,primes_under_20,1)
value = prod_primes
while(not all(value % x == 0 for x in composites_under_20)):
	value += prod_primes
print(value)
