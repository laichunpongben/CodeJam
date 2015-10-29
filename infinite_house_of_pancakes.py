# Google Code Jam
# Google Code Jam 2015
# Qualification Round
# Problem B. Infinite House of Pancakes

# Unsolved

from math import ceil

class TestCase:
    def __init__(self):
        self.initial_diner_count = 0
        self.pancakes = 0
        
    def compute_best_time(self):
        best_time = 0
        pancake_count = sum(self.pancakes)
        
        while (pancake_count > 0):
            print(self.pancakes)
            max_pancake = max(self.pancakes)
            threshold = ceil(max_pancake / 2)
            
            count_over_threshold = sum(1 for x in self.pancakes if x > threshold)
            time_to_threshold = max_pancake - threshold
            
            if (max_pancake == 1):
                self.pancakes = [0 for x in self.pancakes]
                best_time += 1
            elif (count_over_threshold >= time_to_threshold): 
                self.pancakes = [max(x - 1, 0) for x in self.pancakes]
                best_time += 1
            else: 
                for x in range(len(self.pancakes)):
                    if (self.pancakes[x] > threshold):
                        new_pancake = self.pancakes[x] - ceil(self.pancakes[x] / 2)
                        self.pancakes[x] = ceil(self.pancakes[x] / 2)
                        self.pancakes.append(new_pancake)
                best_time += count_over_threshold
            
            pancake_count = sum(self.pancakes)
            
        return best_time

def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if (index % 2 > 0): 
                count += 1
                if (count < n):
                    test_cases[count] = TestCase()
                    initial_diner_count = int(item)
                    test_cases[count].pancakes = [0 for x in range(initial_diner_count)]
            else: 
                p = item.split(' ')
                if (len(p) > 0):
                    for x in range(initial_diner_count):
                        test_cases[count].pancakes[x] = int(p[x])

def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x + 1) + ': ' + str(test_cases[x].compute_best_time()))

test_case_file = open("InfiniteHouseOfPancakes_B-small-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
