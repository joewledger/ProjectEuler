import itertools
import operator

class Prime_Stream:

    def __init__(self):
        self.stored_primes = [2]
            
    def is_prime(self,number):
        if(number < self.stored_primes[-1]):
            return number in self.stored_primes
        else:
            i = 0
            while(self.__getitem__(i) ** 2 <= number):
                if(number % self.stored_primes[i] == 0):
                    return False
                i += 1
            return True

    def get_stored_primes(self):
        return self.stored_primes

    def get_primes_under_n(self,n):
        if(n < self.stored_primes[-1]):
            i = 0
            while(self.stored_primes[i] < n):
                i += 1
            return self.stored_primes[:i]
        else:
            while(n > self.stored_primes[-1]):
                self.__getitem__(len(self.stored_primes))
            return self.stored_primes[:-1]

    def __getitem__(self,index):
        i = self.stored_primes[-1] + 1
        while(len(self.stored_primes) < index + 1):
            if(self.is_prime(i)): self.stored_primes.append(i)
            i += 1
        return self.stored_primes[index]

    def __len__(self):
        return len(self.stored_primes)

class Prime_Utils:

    def __init__(self):
        self.prime_stream = Prime_Stream()

    def prime_factorization(self,number):
        val = number
        prime_index = 0
        factorization = []
        while(val > 1):
            prime_val = self.prime_stream[prime_index]
            if(val % prime_val == 0):
                factorization.append(prime_val)
                val /= prime_val
            else:
                prime_index += 1
        return factorization

    def get_divisor_list(self,number):
        divisor_set = set()
        pf = self.prime_factorization(number)
        for i in xrange(0,len(pf) + 1):
            for product in [reduce(operator.mul,x,1) for x in itertools.combinations(pf,i)]:
                divisor_set.add(product)
        return sorted(list(divisor_set))
        

    #Gets the number of divisors of a number using a generating function
    #Methodology is described at http://mathforum.org/library/drmath/view/56197.html
    def get_num_divisors(self,number):
        pf = self.prime_factorization(number)
        factor_sizes = [1]
        for i in xrange(1,len(pf)):
            if(pf[i] == pf[i - 1]):
                factor_sizes[-1] += 1
            else:
                factor_sizes.append(1)
        generating_function = self.create_generating_function(factor_sizes)
        return sum(generating_function)

    def create_generating_function(self,factor_sizes):
        generating_function= [[1 for x in xrange(0,j + 1)] for j in factor_sizes]
        def multiply_partial_generating_functions(a,b):
            c = [0 for x in xrange(0,len(a) + len(b) - 1)]       
            for a_index,a_value in enumerate(a):
                for b_index, b_value in enumerate(b):
                    c[a_index + b_index] += a_value * b_value
            return c
        return reduce(multiply_partial_generating_functions, generating_function)

    def get_perfect_numbers(self):
        i = 0
        while(True):
            prime = self.prime_stream[i]
            yield (2 ** (prime - 1)) * (2 ** prime - 1)
            i += 1
