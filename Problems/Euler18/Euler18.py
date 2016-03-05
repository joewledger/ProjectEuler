#Project Euler Problem 18/67
#Finds the largest possible sum of all the paths of a Triangle
#Dynamic Programming Approach

import os
import sys

if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])

reader = open("triangle.txt", "rb")
arr = [[int(y) for y in x.strip().split(" ")] for x in reader.readlines()]
reader.close()

def reduce_to_max_path(arr1,arr2):
    arr3 = []
    for i in xrange(0,len(arr2)):
        best_prev = max(arr1[max(i-1,0):min(i,len(arr1) - 1) + 1])
        new_val = arr2[i] + best_prev
        arr3.append(new_val)
    return arr3

print(max(reduce(reduce_to_max_path,arr)))
