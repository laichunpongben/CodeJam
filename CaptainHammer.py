# Google Code Jam
# Google APAC 2016 University Graduates Test
# Practice Round APAC test 2016 
# Problem B. Captain Hammer

from math import asin
from math import degrees

class TestCase:
    def __init__(self, v, d):
        self.velocity = v
        self.distance = d
                
testCaseFile = open("CaptainHammer_B-small-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                v = int(items[0])
                d = int(items[1])
                testCases[index - 1] = TestCase(v, d)
            
def compute_angle(v, d):
    g = 9.8
    return 0.5 * asin(min(g * d / v ** 2, 1))
    
def is_almost_equal(f1, f2, digit):
    return abs(f1 - f2) < 0.1 ** digit
    
def print_all_results():
    for x in range(len(testCases)):
        angle = round(degrees(compute_angle(testCases[x].velocity, testCases[x].distance)), 6)
        if (is_almost_equal(angle, int(angle), 7)): angle = int(angle)
        print('Case #' + str(x + 1) + ': ' + str(angle))
        
def write_all_results():
    testResultFile = open("CaptainHammer.txt", "w")
    for x in range(len(testCases)):
        angle = round(degrees(compute_angle(testCases[x].velocity, testCases[x].distance)), 6)
        if (is_almost_equal(angle, int(angle), 7)): angle = int(angle)
        testResultFile.write('Case #' + str(x + 1) + ': ' + str(angle) + '\n')
    testResultFile.close()
            
initialize_test_cases(lines)
write_all_results()
