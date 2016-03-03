#Project Euler Problem 16
#Calculates the sum of the digits of the number of 2^1000
#Uses method from Euler 13 to add very large numbers

def double(number):
	place = len(number) - 1
	digit = [0] * len(number)
	carry = [0] * len(number)
	while(place >= 0):
		digit[place] = int(number[place]) * 2 % 10
		if(not place + 1 >= len(number)): digit[place] += carry[place + 1]
		carry[place] = int(number[place]) * 2 / 10
		place -= 1
	number = ""
	if(not carry[0] == 0): number = str(carry[0])
	for i in range(0, len(digit)):
		number += str(digit[i])
	return number

original = "2"
exponent = 1
while(exponent < 1000):
	original = double(original)
	exponent += 1
total = 0
for i in range(0,len(original)):
	total += int(original[i])
print total
