# Google Code Jam
# Google Code Jam 2015
# Qualification Round
# Problem A. Standing Ovation

class TestCase:
    def __init__(self):
        self.audienceCount = 0
        self.audience = 0
        
testCaseFile = open("StandingOvation_A-large-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                sMax = int(items[0])
                s = items[1]
                testCases[index - 1] = TestCase()
                testCases[index - 1].audienceCount = sum_digits(s)
                testCases[index - 1].audience = [0 for x in range(sMax + 1)]
                for x in range(sMax + 1):
                    testCases[index - 1].audience[x] = int(s[x])
                    
def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())                    

def compute_friend(testCase):
    standingOvationCount = 0
    friend = 0
    for x in range(len(testCase.audience)):
        if (standingOvationCount >= x): 
            standingOvationCount += testCase.audience[x]
        else: 
            friendRequired = x - standingOvationCount
            friend += friendRequired
            standingOvationCount += testCase.audience[x] + friendRequired
    return friend

def print_all_results():
    for x in range(len(testCases)):
        print('Case #' + str(x + 1) + ': ' + str(compute_friend(testCases[x])))

initialize_test_cases(lines)
print_all_results()
