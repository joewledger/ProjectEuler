#Project Euler Problem #2
#Find sum of even fibonacci numbers under 4 million

import time
time.clock()

def calculate_fibonacci_numbers(limit):
    first = 1
    yield 1
    second = 2
    yield 2
    while(first + second < limit):
        fib = first + second
        yield fib
        first = second
        second = fib

value = sum(x for x in calculate_fibonacci_numbers(4000000) if x % 2 == 0)

print("Answer: %s" % value)
print("Calculation took %s seconds" % str(time.clock()))



