#Project Euler Problem 7
#Finds 10001st prime

import sys
sys.path.append("../../Utils")
sys.path.append("Utils")
import prime_utils as p

stream = p.Prime_Stream()
print(stream[10000])
