#Project Euler Problem 30
#Find the sum of all numbers that can be expressed as the sum of their digits to the 5th power

num_digits = lambda n : num_digits(n / 10) + 1 if n > 10 else 1
nth_digit = lambda number, n : int((number % (10 ** (n + 1))) / (10 ** n))
digit_sum = lambda n : sum(nth_digit(n,x) ** 5 for x in xrange(0, num_digits(n)))

max_check = 354294

print(sum(x for x in xrange(2,max_check) if x == digit_sum(x)))
