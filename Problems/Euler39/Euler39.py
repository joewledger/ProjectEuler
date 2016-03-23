#Project Euler Problem 39
#Description: The perimeter of a right triangle is given as the integer p
#Find the value of p <= 1000 for which there are the most possible combinations of side lengths for the triangle
#Ex. For p=120, there are 3 possible side length combinations: {20,48,52},{24,45,51},{30,40,50}

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import math

#For each value of p: we must check all values of a that could be part of a possible solution
#a <= b <= c, a + b + c = p, and a^2 + b^2 = c^2
#If we let b = a, we can derive a <= p / (2 + sqrt(a))
#So we check all values of a up to this point
#For a to be part of a solution, then the following must be an integer (p(p - 2a)) / 2(p-a)

a_upper_bound = lambda p : int(p / (2 + math.sqrt(2)))
b_remainder = lambda a,p : (p * (p - 2 * a)) % (2 * (p - a))
num_solutions = [sum(1 for a in xrange(1,a_upper_bound(p)) if b_remainder(a,p) == 0) for p in xrange(1,1000)]
print(num_solutions.index(max(num_solutions)) + 1)
