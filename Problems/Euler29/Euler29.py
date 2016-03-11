#Project Euler Problem N
#Description

lower_limit = 2
upper_limit = 100
distinct_powers = set()

for a in xrange(lower_limit,upper_limit + 1):
    for b in xrange(lower_limit,upper_limit + 1):
        distinct_powers.add(a ** b)
print(len(distinct_powers))
