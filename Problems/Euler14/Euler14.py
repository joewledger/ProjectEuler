max_number = 999999
cache = {1 : 0}

next = lambda n : n / 2 if n % 2 == 0 else 3 * n + 1

for i in xrange(2,max_number + 1):
    numbers = [i]
    while(not numbers[-1] in cache):
        numbers.append(next(numbers[-1]))
    c_val = cache[numbers[-1]]
    for x in reversed(numbers):
        cache[x] = c_val
        c_val += 1

print(sorted(cache.iteritems(), key=lambda x : x[1])[-1][0])
