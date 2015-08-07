#Project Euler Problem 10
#Find the sum of all primes below 2 million

maxCheck = 2000000
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
primeSum = 0
for index in range(0, len(primes)):
	if(primes[index]):
		primeSum += index
print(primeSum)