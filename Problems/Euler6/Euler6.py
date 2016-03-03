#Project Euler Problem 6
#Find the difference between the square of sums and the sum of squares for the first 100 natural numbers

sum_of_squares = sum(x ** 2 for x in xrange(1,101))
square_of_sums = sum(xrange(1,101)) ** 2
value = square_of_sums - sum_of_squares

print(value)
