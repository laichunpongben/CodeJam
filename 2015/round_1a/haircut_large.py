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
        current_position = self.position
        barber_available = 0
        
        if (all_same(self.barbers)):
            barber_available = current_position % len(self.barbers)
            if (barber_available == 0): barber_available = len(self.barbers)
            return barber_available
        
        if (current_position > cycle_period): current_position = current_position % cycle_serve
        if (current_position == 0): current_position = cycle_serve
        
        time = int(max(binary_search_time(self.barbers, current_position, cycle_period), 0)) #improved search start position
        already_served = compute_serve_at_time(self.barbers, time)
        current_position = current_position - already_served
        
        if (current_position == 0):
            while (barber_available == 0):
                time += -1
                for index, item in reverse_enum(self.barbers):
                    if (time % item == 0): 
                        barber_available = index + 1
                        break
    
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
     
def reverse_enum(items):
   for index in reversed(range(len(items))):
      yield index, items[index]

def all_same(items):
    return all(x == items[0] for x in items)
     
def compute_serve_at_time(barbers, time):
    if (time == 0): return 0
    else: return sum((time - 1) // x for x in barbers) + len(barbers)
    
def binary_search_time(barbers, position, upper_bound):
    low = 0
    high = upper_bound
    x = int(min(upper_bound, 1e11))
    serve = 0
    count = 0
    
    while (count < 100):
        count += 1
        serve = compute_serve_at_time(barbers, x)
        if (serve > position): 
            high = x
        else: 
            low = x
        x = (low + high) // 2
    return x
    
def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x + 1) + ': ' + str(test_cases[x].compute_barber()))

test_case_file = open("Haircut_B-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
