# Google Code Jam
# Google Code Jam 2015
# Round 1A
# Problem B. Haircut

# Solved

from functools import reduce
from fractions import gcd

class TestCase:
    def __init__(self, p):
        self.position = p
        self.barbers = []
        
    def compute_barber(self):
        cycle_period = lcm(self.barbers)
        cycle_serve = sum(cycle_period // x for x in self.barbers)
        time = 0
        current_position = self.position
        barber_available = 0
        
        if (current_position > cycle_period): current_position = current_position % cycle_serve
        if (current_position == 0): current_position = cycle_serve
        
        while (current_position > 0):
            for x in range(len(self.barbers)):
                if (time % self.barbers[x] == 0): 
                    barber_available = x + 1
                    current_position += -1
                    if (current_position == 0): break
            time += 1
        return barber_available
                
def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if (index % 2 > 0): 
                count += 1
                if (count < n):
                    p = item.split(' ')
                    barber_count = int(p[0])
                    position = int(p[1])
                    test_cases[count] = TestCase(position)
                    test_cases[count].barbers = [0 for x in range(barber_count)]
            else: 
                p = item.split(' ')
                if (len(p) > 0):
                    for x in range(len(test_cases[count].barbers)):
                        test_cases[count].barbers[x] = int(p[x])

def lcm(numbers): 
     def lcm(a, b): 
         return (a * b) // gcd(a, b) 
     return reduce(lcm, numbers)
                        
def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x + 1) + ': ' + str(test_cases[x].compute_barber()))

test_case_file = open("Haircut_B-small-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
