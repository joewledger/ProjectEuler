import os
from os.path import isfile,join

problem_dirs = [x[0] for x in os.walk("Problems")][1:]
for path in problem_dirs:
    if "run.sh" in os.listdir(path):
        print(path)
