#Project Euler Problem 8
#Finds the greatest product of 13 consecutive digits in a 1000 digit number
from operator import mul
import os
import sys

if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])

reader = open("number.txt","rb")
number = reader.readline().strip()
reader.close()

offset = 13
max_prod = lambda x : max(reduce(mul,[int(y) for y in x[i: i+offset]],1) for i in xrange(0,len(x) - offset))
print(max_prod(number))
