#Project Euler Problem 7
#Finds 10001st prime

import Prime_Generator as p_gen

max_n = 200000
value = p_gen.generate_primes(max_n,"eratosthenes")[10000]

print(value)
