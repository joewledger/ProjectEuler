#Project Euler Problem 18/67
#Finds the largest possible sum of all the paths of a Triangle

file = open('triangle.txt','r')
textS = file.readlines()
arrayN = []
for row in range(0, len(textS)):
	arrayN.append([])
	numb = textS[row].split(' ')
	for col in range(0, row + 1):
		arrayN[row].append(int(numb[col]))
weightedValuesP = [0] * 2
weightedValuesP[0] = arrayN[0][0]
weightedValues = weightedValuesP
for row in range(1, len(textS)):
	weightedValues = [0] * (row + 1)
	for col in range(0, row + 1):
		if(col == 0):
			weightedValues[col] = arrayN[row][col] + weightedValuesP[col]
		if(col == row):
			weightedValues[col] = arrayN[row][col] + weightedValuesP[col - 1]
		if(col > 0 and col < row):
			weightedValues[col] = arrayN[row][col] + max(weightedValuesP[col - 1], weightedValuesP[col])
	weightedValuesP = weightedValues

print(max(weightedValues))
