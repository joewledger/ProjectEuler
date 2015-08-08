#Project Euler Problem #4
#Find the largest palindrome made from the product of two 3-digit numbers

import time
time.clock()

def all_products_of_three_digit_numbers():
    for x in xrange(1000,100,-1):
        for y in range(1000,100,-1):
            yield x * y

value = max(product for product in all_products_of_three_digit_numbers() if str(product)[:3] == str(product)[:2:-1])

print("Answer: %s" % value)
print("Calculation took %s seconds" % str(time.clock()))
