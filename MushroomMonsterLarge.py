# Google Code Jam
# Google Code Jam 2015
# Round 1A
# Problem A. Mushroom Monster

class TestCase:
    def __init__(self):
        self.mushrooms = []
        
testCaseFile = open("MushroomMonster_A-large-practice.in", "r")
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
                    testCases[count] = TestCase()
                    period = int(item)
                    testCases[count].mushrooms = [0 for x in range(period)]
            else: 
                p = item.split(' ')
                if (len(p) > 0):
                    for x in range(len(testCases[count].mushrooms)):
                        testCases[count].mushrooms[x] = int(p[x])
                        
def compute_method1_min(testCase):
    mushroomEaten = 0
    for x in range(len(testCase.mushrooms) - 1):
        mushroomEaten += max(testCase.mushrooms[x] - testCase.mushrooms[x + 1], 0)
    return mushroomEaten

def compute_method2_rate(testCase):
    rate = 0
    for x in range(len(testCase.mushrooms) - 1):
        rate = max(testCase.mushrooms[x] - testCase.mushrooms[x + 1], rate)
    return rate
    
def compute_method2_min(testCase):
    mushroomEaten = 0
    rate = compute_method2_rate(testCase)
    #print(rate)
    for x in range(len(testCase.mushrooms) - 1):
        mushroomEaten += min(testCase.mushrooms[x], rate)
    return mushroomEaten

def print_all_results():
    for x in range(len(testCases)):
        #print(testCases[x].mushrooms)
        y = compute_method1_min(testCases[x])
        z = compute_method2_min(testCases[x])
        print('Case #' + str(x + 1) + ': ' + str(y) + ' ' + str(z))
    
initialize_test_cases(lines)
print_all_results()
