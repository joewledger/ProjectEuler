#Project Euler Problem 9
#Finds the product of the pythagorean triple whose terms add up to 1000

answer = 0
a = 0
for i in range(1, 1000):
	a = i
	b = 1
	c = 999 - i
	for x in range(0, c / 2):
		b += 1
		c -= 1
		if(a * a + b * b == c * c):
			answer = a * b * c
print(answer)
