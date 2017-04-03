#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2015
# Qualification Round
# Problem A. Standing Ovation

# Solved

class TestCase:
    def __init__(self):
        self.audience_count = 0
        self.audience = 0

    def compute_friend(self):
        standing_ovation_count = 0
        friend = 0
        for x in range(len(self.audience)):
            if (standing_ovation_count >= x):
                standing_ovation_count += self.audience[x]
            else:
                friend_required = x - standing_ovation_count
                friend += friend_required
                standing_ovation_count += self.audience[x] + friend_required
        return friend

def initialize_test_cases(lines):
    global test_cases
    for index, item in enumerate(lines):
        if index > 0:
            items = item.split(' ')
            if (len(items) > 1):
                s_max = int(items[0])
                s = items[1]
                test_cases[index - 1] = TestCase()
                test_cases[index - 1].audience_count = sum_digits(s)
                test_cases[index - 1].audience = [0 for x in range(s_max + 1)]
                for x in range(s_max + 1):
                    test_cases[index - 1].audience[x] = int(s[x])

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x + 1) + ': ' + str(test_cases[x].compute_friend()))

test_case_file = open("StandingOvation_A-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
