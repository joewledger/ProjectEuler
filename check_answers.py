import os
from os.path import isfile,join
import multiprocessing
import time
import subprocess
import re


def main():
    max_seconds = 1
    answer_dict = get_answer_dictionary()

    problem_dirs = [x[0] for x in os.walk("Problems")][1:]
    for path in problem_dirs:
        if "run.sh" in os.listdir(path):
            p = multiprocessing.Process(target=run_problem, name="",args=(path,answer_dict,))
            p.start()

            p.join(max_seconds)

            time.sleep(max_seconds)
            if p.is_alive():
                print("Terminating: %s" % path)
                p.terminate()
                p.join()
                proc = subprocess.Popen("ps aux | pgrep -f %s" % path, stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                for s in out.split("\n")[:-1]:
                    DEVNULL = open(os.devnull, 'wb')
                    subprocess.Popen("kill -9 %d" % int(s), stdout=DEVNULL, stderr=DEVNULL,shell=True).communicate()
                    DEVNULL.close()

def run_problem(path,answer_dict):
    run_file = "%s/%s" % (path,"run.sh")
    problem_number = int(re.search(r'\d+$', path).group(0))
    correct_answer = answer_dict[problem_number]

    os.system("chmod +x %s" % run_file)
    proc = subprocess.Popen("time -f %%E %s %s" % (run_file,path), stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if not err:
        print("Problem: %d\tCorrect Answer: %d\tProgram Answer: %s" % (problem_number, correct_answer,out.strip()))
    else:
        print("Problem: %d\t Error: %s" % (problem_number,err))

def get_answer_dictionary():
    answers = {}
    reader = open("solved.txt", "rb")
    for line in reader.readlines():
        if(not line[0] == "#"):
            l = line.split(":")
            answers[int(l[0])] = int(l[1])
    return answers

if __name__ == "__main__":
    main()  
