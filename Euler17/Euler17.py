#Project Euler Problem 17
#Counts the number of letters in the numbers 1-1000(inclusive)

words = ["zero", "one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen", "twenty"]
for i in range(21, 1001):
	words.append("")
words[30] = "thirty"
words[40] = "forty"
words[50] = "fifty"
words[60] = "sixty"
words[70] = "seventy"
words[80] = "eighty"
words[90] = "ninety"
for i in range(21, 1001):
	if(i < 100 and not i%10 == 0):
		words[i] = words[i - i%10] + words[i%10]
	if(i > 99 and i < 1000):
		words[i] = words[i/100] + "hundred"
		if(not i%100 == 0):
			words[i] += "and" + words[i%100]
words[1000] = "onethousand"
letterCount = 0
for i in range(1,1001):
	letterCount += len(words[i])
print(letterCount)
