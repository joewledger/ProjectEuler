import Src.Prime_Generator as p_gen

def first_test():
    reader = open("Res/Tests/1000_primes.txt","rb")
    primes = []
    for row in reader.readlines():
        for entry in row.strip().split(" "):
            if(entry != ""):
                primes.append(entry)
    assert p_gen.generate_primes_sieve_of_atkin(7920) == primes
    assert p_gen.generate_primes_sieve_of_sundaram(7920) == primes
    assert p_gen.generate_primes_sieve_of_eratosthenes(7920) == primes