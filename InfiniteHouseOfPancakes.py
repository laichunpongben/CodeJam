# Google Code Jam
# Google Code Jam 2015
# Qualification Round
# Problem B. Infinite House of Pancakes

from math import ceil

class TestCase:
    def __init__(self):
        self.initialDinerCount = 0
        self.pancakes = 0
        
testCaseFile = open("InfiniteHouseOfPancakes_B-small-practice.in", "r")
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
                    initialDinerCount = int(item)
                    testCases[count].pancakes = [0 for x in range(initialDinerCount)]
            else: 
                p = item.split(' ')
                if (len(p) > 0):
                    for x in range(initialDinerCount):
                        testCases[count].pancakes[x] = int(p[x])
                        
def compute_best_time(testCase):
    bestTime = 0
    pancakeCount = sum(testCase.pancakes)
    
    while (pancakeCount > 0):
        print(testCase.pancakes)
        maxPancake = max(testCase.pancakes)
        threshold = ceil(maxPancake / 2)
        
        countOverThreshold = sum(1 for x in testCase.pancakes if x > threshold)
        timeToThreshold = maxPancake - threshold
        
        if (maxPancake == 1):
            testCase.pancakes = [0 for x in testCase.pancakes]
            bestTime += 1
        elif (countOverThreshold >= timeToThreshold): 
            testCase.pancakes = [max(x - 1, 0) for x in testCase.pancakes]
            bestTime += 1
            #testCase.pancakes = [0 for x in testCase.pancakes]
            #bestTime += maxPancake
        else: 
            for x in range(len(testCase.pancakes)):
                if (testCase.pancakes[x] > threshold):
                    newPancake = testCase.pancakes[x] - ceil(testCase.pancakes[x] / 2)
                    testCase.pancakes[x] = ceil(testCase.pancakes[x] / 2)
                    testCase.pancakes.append(newPancake)
            bestTime += countOverThreshold
        
        pancakeCount = sum(testCase.pancakes)
        #print(threshold)
        #print(countOverThreshold)
        #print(timeToThreshold)
        
    
    return bestTime

def print_all_results():
    for x in range(len(testCases)):
        print('Case #' + str(x + 1) + ': ' + str(compute_best_time(testCases[x])))

initialize_test_cases(lines)
print_all_results()
#print(compute_best_time(testCases[68]))
