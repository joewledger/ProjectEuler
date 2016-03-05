#Project Euler Problem 3
#Finds the largest prime factor of 600851475143

import sys
sys.path.append("../../Utils")
sys.path.append("Utils")
import prime_utils as p

util = p.Prime_Utils()
prime_factors = util.prime_factorization(600851475143)
print(prime_factors[-1])
