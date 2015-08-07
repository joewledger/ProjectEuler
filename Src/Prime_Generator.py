"""
This module generates prime numbers.
More specifically, it implements the following algorithms
    Sieve of Eratosthenes
    Sieve of Atkin
    Sieve of Sundaram
"""

def generate_primes(max_n,sieve="atkin"):
    if(sieve=="atkin"):
        return generate_primes_sieve_of_atkin(max_n)
    elif(sieve == "eratosthenes"):
        return generate_primes_sieve_of_eratosthenes(max_n)
    elif(sieve == 'sundaram'):
        return generate_primes_sieve_of_sundaram(max_n)
    else:
        raise Exception(msg="Incorrect sieve type provided")

def generate_primes_sieve_of_atkin(max_n):
    results = [2,3,5]
    sieve_list = (False for x in xrange(0,max_n + 1))
    return results

def generate_primes_sieve_of_eratosthenes(max_n):
    return None

def generate_primes_sieve_of_sundaram(max_n):
    return None

print(type(y))