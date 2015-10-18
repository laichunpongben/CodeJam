# Google Code Jam
# Google Code Jam 2015
# Round 1A
# Problem B. Haircut

from functools import reduce
from fractions import gcd

class TestCase:
    def __init__(self, p):
        self.position = p
        self.barbers = []
        
testCaseFile = open("Haircut_B-large-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if (index % 2 > 0): 
                count += 1
                if (count < n):
                    p = item.split(' ')
                    barberCount = int(p[0])
                    position = int(p[1])
                    testCases[count] = TestCase(position)
                    testCases[count].barbers = [0 for x in range(barberCount)]
            else: 
                p = item.split(' ')
                if (len(p) > 0):
                    for x in range(len(testCases[count].barbers)):
                        testCases[count].barbers[x] = int(p[x])

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
    
def binary_search_time(barbers, position, upperBound):
    low = 0
    high = upperBound
    x = int(min(upperBound, 1e11))
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
                        
def compute_barber(testCase):
    cyclePeriod = lcm(testCase.barbers)
    cycleServe = sum(cyclePeriod // x for x in testCase.barbers)
    currentPosition = testCase.position
    barberAvailable = 0
    
    if (all_same(testCase.barbers)):
        barberAvailable = currentPosition % len(testCase.barbers)
        if (barberAvailable == 0): barberAvailable = len(testCase.barbers)
        return barberAvailable
    
    if (currentPosition > cyclePeriod): currentPosition = currentPosition % cycleServe
    if (currentPosition == 0): currentPosition = cycleServe
    
    time = int(max(binary_search_time(testCase.barbers, currentPosition, cyclePeriod), 0)) #improved search start position
    alreadyServed = compute_serve_at_time(testCase.barbers, time)
    currentPosition = currentPosition - alreadyServed
    
    if (currentPosition == 0):
        while (barberAvailable == 0):
            time += -1
            for index, item in reverse_enum(testCase.barbers):
                if (time % item == 0): 
                    barberAvailable = index + 1
                    break

    while (currentPosition > 0):
        for x in range(len(testCase.barbers)):
            if (time % testCase.barbers[x] == 0): 
                barberAvailable = x + 1
                currentPosition += -1
                if (currentPosition == 0): break
        time += 1
    return barberAvailable
    
def print_all_results():
    for x in range(len(testCases)):
        print('Case #' + str(x + 1) + ': ' + str(compute_barber(testCases[x])))

initialize_test_cases(lines)
print_all_results()
