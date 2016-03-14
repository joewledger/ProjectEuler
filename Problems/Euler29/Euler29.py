#Project Euler Problem 29
#Find the number of distinct integers of the form a^b for a,b in range[2,100)

lower_limit = 2
upper_limit = 100
distinct_powers = set()

for a in xrange(lower_limit,upper_limit + 1):
    for b in xrange(lower_limit,upper_limit + 1):
        distinct_powers.add(a ** b)
print(len(distinct_powers))
