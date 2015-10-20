# Google Code Jam
# Google Code Jam 2014
# Qualification Round 2014
# Problem B. Cookie Clicker Alpha

class TestCase:
    def __init__(self, c, f, x):
        self.initialReturn = 2
        self.cookieFarmCost = c
        self.cookieFarmReturn = f
        self.winningCondition = x
        self.currentStock = 0
        self.currentReturn = self.initialReturn
                
testCaseFile = open("CookieClickerAlpha_B-large-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                c = float(items[0])
                f = float(items[1])
                x = float(items[2])
                testCases[index - 1] = TestCase(c, f, x)
                
def compute_min_time_to_win(testCase):
    time = 0
    while (testCase.currentStock < testCase.winningCondition):
        winningTimeIfNoAction = compute_time_to_win_if_no_action(testCase)
        winningTimeIfBuildCookieFarm = compute_time_to_win_if_build_cookie_farm(testCase)
        if (winningTimeIfNoAction <= winningTimeIfBuildCookieFarm):
            time += winningTimeIfNoAction
            testCase.currentStock += winningTimeIfNoAction * testCase.currentReturn
        else:
            timeToBuildCookieFarm = compute_time_to_build_cookie_farm(testCase)
            time += timeToBuildCookieFarm
            testCase.currentStock += timeToBuildCookieFarm * testCase.currentReturn
            build_cookie_farm(testCase)
    return time
    
def compute_time_to_build_cookie_farm(testCase):
    return (testCase.cookieFarmCost - testCase.currentStock) / testCase.currentReturn
    
def compute_time_to_win_if_no_action(testCase):
    return (testCase.winningCondition - testCase.currentStock) / testCase.currentReturn

def compute_time_to_win_if_build_cookie_farm(testCase):
    return compute_time_to_build_cookie_farm(testCase) + testCase.winningCondition / (testCase.currentReturn + testCase.cookieFarmReturn)

def build_cookie_farm(testCase):
    if (testCase.currentStock >= testCase.cookieFarmCost):
        testCase.currentStock += -1 * testCase.cookieFarmCost
        testCase.currentReturn += testCase.cookieFarmReturn

def print_all_results():
    for x in range(len(testCases)):
        winningTime = round(compute_min_time_to_win(testCases[x]), 7)
        print('Case #' + str(x + 1) + ': ' + "%.7f" % winningTime)

initialize_test_cases(lines)
print_all_results()
