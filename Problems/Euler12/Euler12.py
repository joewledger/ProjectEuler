#Project Euler Problem 12
#Finds the first triangle number to have over 500 divisors
import sys
sys.path.append("../..")
from Utils import prime_utils as p

def triangle_numbers():
    i = 1
    tn = 0
    while(True):
        tn += i
        i += 1
        yield tn

a = triangle_numbers()
util = p.Prime_Utils()
tn = a.next()
while(util.get_num_divisors(tn) < 500):
    tn = a.next()
print(tn)
