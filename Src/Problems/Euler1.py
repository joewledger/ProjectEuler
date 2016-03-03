#Project Euler Problem #1
#List the sum of all multiples of 3 and 5 below 1000

import time
time.clock()

value = sum(x for x in xrange(1,1000) if x % 3 == 0 or x % 5 == 0)

print("Answer: %s" % value)
print("Calculation took %s seconds" % str(time.clock()))