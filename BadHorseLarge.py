# Google Code Jam
# Google APAC 2016 University Graduates Test
# Practice Round APAC test 2016 
# Problem A. Bad Horse

import itertools
from random import shuffle

class TestCase:
    def __init__(self):
        self.players = set()
        self.troublePairs = []
        
testCaseFile = open("BadHorse_A-small-practice-2.in", "r")
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
    set2 = set()
    unsolvedPairs = testCase.troublePairs
    count = 0
    
    shuffle(unsolvedPairs)
    set1.add(unsolvedPairs[0][0])
    set2.add(unsolvedPairs[0][1])
    unsolvedPairs.remove(unsolvedPairs[0])
    unsolvedPairs.sort()
    
    while (len(unsolvedPairs) > 0 and count < 100):
        count += 1
        for pair in unsolvedPairs:
            if ((pair[0] in set1 and pair[1] not in set1) or (pair[1] in set2 and pair[0] not in set2)):
                set1.add(pair[0])
                set2.add(pair[1])
                unsolvedPairs.remove(pair)
            elif ((pair[0] in set2 and pair[1] not in set2) or (pair[1] in set1 and pair[0] not in set1)):
                set1.add(pair[1])
                set2.add(pair[0])
                unsolvedPairs.remove(pair)
            elif ((pair[0] in set1 and pair[1] in set1) or (pair[0] in set2 and pair[1] in set2)):
                return False

    return True
                
def print_all_results():
    for x in range(len(testCases)):
        if (is_safe_set_exist(testCases[x])): print('Case #' + str(x + 1) + ': Yes')
        else: print('Case #' + str(x + 1) + ': No')

initialize_test_cases(lines)
print_all_results()
