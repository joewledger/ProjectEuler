#Project Euler Problem 19
#Counts the number of sundays that fell on the first of the mounth in the 20th century(1/1/1901 - 12/31/2000)
#1/1/1900 was a monday
#leap years occur on years evenly divisible by 4 unless it is a century in which case it must be divisible by 400
#30 days have september, april, june and november, all the rest have 31, except february which has 28/29

#monday = 0. tuesday = 1, wed = 2, thur = 3, fri = 4, sat = 5, sun = 6
days = [0] * (366 * 101)
currD = 0
currV = 0
while(currD < len(days)):
	days[currD] = currV
	currD += 1
	currV += 1
	if(currV == 7): currV = 0
day = 0
month = 0
year = 1900
firstCount = 0
while(year < 2001):
	if(month == 0 or month == 2 or month == 4 or month == 6 or month == 7 or month == 9 or month == 11): day += 31
	if(month == 3 or month == 5 or month == 8 or month == 10): day += 30
	if(month == 1):
		if(year%4 == 0 and not year == 1900): day += 29
		else: day += 28
	month += 1
	if(month == 12):
		month = 0
		year += 1
	if(days[day] == 6 and year > 1900): firstCount += 1
print firstCount