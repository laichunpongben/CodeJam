# Google Code Jam
# Practice Contests
# Practice Contest
# Problem A. Old Magician

# Solved

import random

class TestCase:
    def __init__(self, w, b):
        self.white = w
        self.black = b
        
    def compute_last_ball_color(self):
        oddEven = (self.black % 2)
        return {
            0: "WHITE",
            1: "BLACK",
        }[oddEven]

def initialize_test_cases(lines):
    global test_cases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                w = int(items[0])
                b = int(items[1])
                test_cases[index - 1] = TestCase(w, b)

def print_all_results():
    for x in range(len(test_cases)):
        print("Case #" + str(x+1) + ": " + test_cases[x].compute_last_ball_color())

test_case_file = open("OldMagician_A-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [[0 for x in range(2)] for x in range(n)]
initialize_test_cases(lines)
print_all_results()
