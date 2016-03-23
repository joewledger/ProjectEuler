#Project Euler Problem 25
#Description: Find the index of the first term in the Fibbonacci sequence to contain 1000 digits

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

import integer_utils

def generate_fibonacci_sequence():
    elements = [0,0,1]
    while(True):
        yield elements[2]
        elements = elements[1:]
        elements.append(sum(elements))
        
digit_length = lambda n : len(integer_utils.convert_int_to_digit_list(n))

g = (i + 1 for i,f in enumerate(generate_fibonacci_sequence()) if digit_length(f) > 999)
print(g.next())
