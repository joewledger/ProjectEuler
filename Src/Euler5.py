#Project Euler Problem 5
#Finds the smallest number evenly divisible by each of the numbers 1-20

satisfied = False
a = 20
while(not satisfied):
	a += 20
	check = True
	cN = 1
	while(cN < 21 and check == True):
		if(not a%cN == 0):
			check = False
		cN += 1
	if(check == True):
		satisfied = True
		print(a)