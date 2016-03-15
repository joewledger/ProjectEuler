#Project Euler Problem 42
#Description: Count the number of triangle words in the file words.txt
#A triangle word is a word whose summation of its characters (A = 1, B = 2, C = 3, ...) is a member of the triangle sequence
#Triange sequence: n * (n + 1) / 2 for all positive integer values of n

import os
import sys
if(len(sys.argv) > 1):
    os.chdir(sys.argv[1])
sys.path.append("../../Utils")
sys.path.append("Utils")

reader = open("words.txt","rb")
words = reader.readline().strip().replace("\"","").split(",")
reader.close()

triangle_numbers = {n * (n + 1) / 2 for n in xrange(1,1000)}

word_sum = lambda word : sum([ord(x) - 64 for x in word])

print(sum(1 for word in words if word_sum(word) in triangle_numbers))
