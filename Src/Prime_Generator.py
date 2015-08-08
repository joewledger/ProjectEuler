"""
This module generates prime numbers.
More specifically, it implements the following algorithms
    Sieve of Eratosthenes
    Sieve of Atkin
    Sieve of Sundaram
"""

import math

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
    """
    Implements the Sieve of Atkin algorithm for finding primes.
    Details can be found at https://en.wikipedia.org/wiki/Sieve_of_Atkin
    :param max_n: The maximum value to find primes up to.
    :return: A complete list of all primes in range(2,max_n)
    """

    results = [2,3,5]
    sieve = (False for x in xrange(1,max_n + 1))
    sieve = flip_entries_atkin(sieve)
    condensed_prime_candidates = (i + 1 for i,x in enumerate(sieve) if x)
    final_prime_candidates = reduce_prime_candidates_atkin(condensed_prime_candidates)
    results.extend([x for x in final_prime_candidates])
    return results

def flip_entries_atkin(sieve):
    """
    This method performs preprocessing for the Sieve of Atkin method.
    It will flip each element of a boolean array a certain number of times depending on certain criteria.
    See https://en.wikipedia.org/wiki/Sieve_of_Atkin for details on what these criteria are.
    :param sieve: A list or generator of boolean values (should all be False initially.)
    :return: A generator of boolean values
    """
    for n,is_prime in enumerate(sieve):
        number = n + 1
        remainder = number % 60
        num_flips = 0
        if(remainder in [1,13,17,29,37,41,49,53]):
            #Calculate the number of solutions to 4x^2 + y^2 = number
            num_flips = sum(1 for x in xrange(1,number) if math.sqrt(max(- 4 * x ** 2 + number,.01)).is_integer())
        elif(remainder in [7,19,31,43]):
            #Calculate the number of solutions to 3x^2 + y^2 = number
            num_flips = sum(1 for x in xrange(1,number) if math.sqrt(max(- 3 * x ** 2 + number,.01)).is_integer())
        elif(remainder in [11,23,47,59]):
            #Calculate the number of solutions to 3x^2 - y^2 = number, where x > y
            calc = lambda x : math.sqrt(max(3 * x ** 2 - number,.01))
            num_flips = sum(1 for x in xrange(1,number) if calc(x).is_integer() and x > calc(x))
        yield (num_flips % 2 == 1)


def reduce_prime_candidates_atkin(condensed_prime_candidates):
    marked_squares = []
    for candidate in condensed_prime_candidates:
        if(not any(candidate % x == 0 for x in marked_squares)):
            marked_squares.append(candidate ** 2)
            yield candidate

def generate_primes_sieve_of_eratosthenes(max_n):
    return None

def generate_primes_sieve_of_sundaram(max_n):
    return None