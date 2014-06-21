#Project Euler Problem 12
#Finds the first triangle number to have over 500 divisors
#Really inefficient, should work on finding better solution

#calculate triangle numbers
triangles = [1]
for i in range(1, 20006):
	triangles.append(i + 1 + triangles[i - 1])
numDivisors = 0

#calculate prime numbers up to 100000
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
primesL = []
for i in range(0, len(primes)):
	if(primes[i]): primesL.append(i)
#use exponent rule to find number of divisiors
a = 2000
numDivisors = 1
while(numDivisors < 501):
	numDivisors = 1
	numb = triangles[a]
	divisors = [0] * len(primesL)
	while(not numb == 1):		
		for i in range(0,len(primesL)):
			if(numb%primesL[i] == 0):
				divisors[i] += 1
				numb /= primesL[i]
	for i in range(0,len(divisors)):
		if(divisors[i] > 0):
			numDivisors *= (divisors[i] + 1)
	a += 1
print(triangles[a -1])