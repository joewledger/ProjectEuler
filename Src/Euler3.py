#Project Euler Problem 3
#Finds the largest prime factor of 600851475143
#Uses sieve of eratosthenes
from time import time
t1 = time()


maxCheck = 100000
primes = [False, False, True, True, False, True]
for index in range(6,maxCheck):
	primes.append(True)
for index in range(2, maxCheck):
	if(primes[index] == True):
		i2 = index
		i2 += index
		while(i2 < maxCheck):
			primes[i2] = False
			i2 += index
a = maxCheck - 1
satisfy = False
while(a > 0):
	if(primes[a] == True):
		if(600851475143%a == 0):
			print(a)
	a -= 1

t2 = time()
print((t2 - t1))