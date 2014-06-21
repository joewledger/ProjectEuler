#Project Euler Problem 15
#Finds number of lattice paths that go through a 20x20 grid

#brute force
count = 0
size = 20
array = [0] * size
while(not array[0] > size):
	count += 1
	array[size - 1] += 1
	satisfied = False
	numb = size - 1
	while(not satisfied):
		if(array[numb] <= size): satisfied = True
		else: 
			numb -= 1
			if(array[numb] <= size): 
				array[numb] += 1
				for i in range(numb, len(array)):
					array[i] = array[numb]
		if(array[0] > size): satisfied = True
print count	



