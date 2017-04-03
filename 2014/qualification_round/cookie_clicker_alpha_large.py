#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2014
# Qualification Round 2014
# Problem B. Cookie Clicker Alpha

# Solved

class TestCase:
    def __init__(self, c, f, x):
        self.initial_return = 2
        self.cookie_farm_cost = c
        self.cookie_farm_return = f
        self.winning_condition = x
        self.current_stock = 0
        self.current_return = self.initial_return

    def compute_min_time_to_win(self):
        time = 0
        while (self.current_stock < self.winning_condition):
            winning_time_if_no_action = self.compute_time_to_win_if_no_action()
            winning_time_if_build_cookie_farm = self.compute_time_to_win_if_build_cookie_farm()
            if (winning_time_if_no_action <= winning_time_if_build_cookie_farm):
                time += winning_time_if_no_action
                self.current_stock += winning_time_if_no_action * self.current_return
            else:
                time_to_build_cookie_farm = self.compute_time_to_build_cookie_farm()
                time += time_to_build_cookie_farm
                self.current_stock += time_to_build_cookie_farm * self.current_return
                self.build_cookie_farm()
        return time

    def compute_time_to_build_cookie_farm(self):
        return (self.cookie_farm_cost - self.current_stock) / self.current_return

    def compute_time_to_win_if_no_action(self):
        return (self.winning_condition - self.current_stock) / self.current_return

    def compute_time_to_win_if_build_cookie_farm(self):
        return self.compute_time_to_build_cookie_farm() + self.winning_condition / (self.current_return + self.cookie_farm_return)

    def build_cookie_farm(self):
        if (self.current_stock >= self.cookie_farm_cost):
            self.current_stock += -1 * self.cookie_farm_cost
            self.current_return += self.cookie_farm_return

def initialize_test_cases(lines):
    global test_cases
    for index, item in enumerate(lines):
        if index > 0:
            items = item.split(' ')
            if (len(items) > 1):
                c = float(items[0])
                f = float(items[1])
                x = float(items[2])
                test_cases[index - 1] = TestCase(c, f, x)

def print_all_results():
    for x in range(len(test_cases)):
        winning_time = round(test_cases[x].compute_min_time_to_win(), 7)
        print('Case #' + str(x + 1) + ': ' + "%.7f" % winning_time)

test_case_file = open("CookieClickerAlpha_B-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
