# Google Code Jam
# Google APAC 2016 University Graduates Test
# Practice Round APAC test 2016 
# Problem A. Bad Horse

import itertools

class TestCase:
    def __init__(self):
        self.players = set()
        self.troublePairs = []
        
testCaseFile = open("BadHorse_A-small-practice-1.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if item.isdigit(): 
                count += 1
                testCases[count] = TestCase()
            else: 
                p = item.split(' ')
                if (len(p) > 1):
                    testCases[count].players.add(p[0])
                    testCases[count].players.add(p[1])
                    testCases[count].troublePairs.append(p)

def is_safe_set_exist(testCase):
    players = testCase.players
    set1 = set()
    set2 = set(players)
    setSize = len(players)
    for x in range(int(setSize / 2) + 1):
        for subset in itertools.combinations(players, x):
            is_safe = True
            set1 = set()
            set2 = set(players)
            for y in subset:
                set1.add(y)
                set2.discard(y)
            for pair in testCase.troublePairs:
                if (pair[0] in set1) and (pair[1] in set1): 
                    is_safe = False
                    break
                elif (pair[0] in set2) and (pair[1] in set2): 
                    is_safe = False
                    break
            if (is_safe): return True
    return False
                
def print_all_results():
    for x in range(len(testCases)):
        if (is_safe_set_exist(testCases[x])): print('Case #' + str(x + 1) + ': Yes')
        else: print('Case #' + str(x + 1) + ': No')
        
initialize_test_cases(lines)
print_all_results()
