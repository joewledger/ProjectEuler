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
    sieve = (False for x in xrange(1,max_n + 1))
    sieve = flip_entries_atkin(sieve)
    condensed_prime_candidates = (i + 1 for i,x in enumerate(sieve) if x)

    #final_prime_candidates = reduce_prime_candidates_atkin(condensed_prime_candidates)
    #results.extend([x for x in final_prime_candidates])
    #return results

def flip_entries_atkin(sieve):
    for n,is_prime in enumerate(sieve):
        number = n + 1
        remainder = number % 60
        if(remainder in [1,13,17,29,37,41,49,53]):
            #do flip operation 1
            yield False
        elif(remainder in [7,19,31,43]):
            #do flip operation 2
            yield False
        elif(remainder in [11,23,47,59]):
            #do flip operation 3
            yield False
        else:
            yield False


def reduce_prime_candidates_atkin(condensed_prime_candidates):
    return None

def generate_primes_sieve_of_eratosthenes(max_n):
    return None

def generate_primes_sieve_of_sundaram(max_n):
    return None

generate_primes_sieve_of_atkin(100)