#Project Euler Problem 7
#Finds 10001st prime

maxCheck = 200000
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
primeCount = 0
for index in range(0, len(primes)):
	if(primes[index]): primeCount += 1
	if(primeCount == 10001 and primes[index]): print(index)
