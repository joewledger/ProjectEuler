#Project Euler Problem 3
#Finds the largest prime factor of 600851475143
#Uses sieve of eratosthenes
from time import time
#t1 = time()
import Prime_Generator as p_gen
import time

time.clock()
primes = p_gen.generate_primes(10000,sieve="eratosthenes")
print("Answer: %s" % str(max(prime for prime in primes if 600851475143 % prime == 0)))
print("Calculation took %s seconds" % str(time.clock()))