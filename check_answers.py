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
    for path in sorted(problem_dirs, key = lambda x: parse_problem_number(x)):
        prob_num = parse_problem_number(path)
        if "run.sh" in os.listdir(path):
            

            p = multiprocessing.Process(target=run_problem, name="",args=(path,prob_num,answer_dict,))
            p.start()

            p.join(max_seconds)

            time.sleep(max_seconds)
            if p.is_alive():
                terminate_euler_process(path,prob_num, p)
        else:
            pretty_print_status(prob_num, "No run.sh script found")

def terminate_euler_process(path,prob_num,process):
    pretty_print_status(prob_num,"Terminated early")
    process.terminate()
    process.join()
    pkill = subprocess.Popen("ps aux | pgrep -f %s" % path, stdout=subprocess.PIPE, shell=True)
    (out, err) = pkill.communicate()
    for s in out.split("\n")[:-1]:
        DEVNULL = open(os.devnull, 'wb')
        subprocess.Popen("kill -9 %d" % int(s), stdout=DEVNULL, stderr=DEVNULL,shell=True).communicate()
        DEVNULL.close()


def run_problem(path,prob_num,answer_dict):
    run_file = "%s/%s" % (path,"run.sh")
    try:
        correct_answer = answer_dict[prob_num]
    except KeyError:
        pretty_print_status(prob_num, "Correct Answer not Specified")
        return

    os.system("chmod +x %s" % run_file)
    DEVNULL = open(os.devnull, 'wb')
    proc = subprocess.Popen("time -f %%E %s %s" % (run_file,path), stdout=subprocess.PIPE,stderr=DEVNULL, shell=True)
    DEVNULL.close()
    (out, err) = proc.communicate()
    try:
        out = int(out.strip())
        correct = "Correct" if (correct_answer == out) else "Incorrect"
        pretty_print_status(prob_num, "%s (%d,%d)" % (correct, correct_answer, out))
    except ValueError:
        pretty_print_status(prob_num,"Did not provide numeric answer")

def get_answer_dictionary():
    answers = {}
    reader = open("solved.txt", "rb")
    for line in reader.readlines():
        if(not line[0] == "#"):
            l = line.split(":")
            answers[int(l[0])] = int(l[1])
    return answers

def parse_problem_number(path):
    return int(re.search(r'\d+$', path).group(0))

def pretty_print_status(prob_num, message):
    print("Problem: %d\t%s" % (prob_num,message))

if __name__ == "__main__":
    main()  
