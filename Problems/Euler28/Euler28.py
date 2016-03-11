#Project Euler Problem 28
#Find the diagonal sum of a 1001x1001 spiral grid

grid_size = 1001
total = 1
curr = 1
for i in xrange(1,grid_size / 2 + 1):
    for j in xrange(0,4):
        curr += 2 * i
        total += curr
print(total)
