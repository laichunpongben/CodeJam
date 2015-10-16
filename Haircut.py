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
        
testCaseFile = open("Haircut_B-small-practice.in", "r")
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
                        
def compute_barber(testCase):
    cyclePeriod = lcm(testCase.barbers)
    cycleServe = sum(cyclePeriod / x for x in testCase.barbers)
    time = 0
    currentPosition = testCase.position
    barberAvailable = 0
    
    if (currentPosition > cyclePeriod): 
        currentPosition = ? % ?
        time = int(? / ?)
    while (currentPosition > 0):
        for x in range(len(testCase.barbers)):
            if (time % testCase.barbers[x] == 0): 
                barberAvailable = x + 1
                currentPosition += -1
                print(time)
                if (currentPosition == 0): break
        time += 1
    return barberAvailable
    
def print_all_results():
    for x in range(len(testCases)):
        print('Case #' + str(x + 1) + ': ' + str(compute_barber(testCases[x])))

initialize_test_cases(lines)
#print_all_results()
for x in range(1):
    print(compute_barber(testCases[x]))


print(lcm(testCases[0].barbers))