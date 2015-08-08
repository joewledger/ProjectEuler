import Src.Prime_Generator as p_gen

def first_test():
    reader = open("Res/Tests/1000_primes.txt","rb")
    primes = []
    for row in reader.readlines():
        for entry in row.strip().split(" "):
            if(entry != ""):
                primes.append(int(entry))
    atkin_primes = p_gen.generate_primes(7920,sieve="atkin")
    sundaram_primes = p_gen.generate_primes(7920,sieve="sundaram")
    eratosthenes_primes = p_gen.generate_primes(7920,sieve="eratosthenes")
    assert atkin_primes == primes
    assert sundaram_primes == primes
    assert eratosthenes_primes == primes
