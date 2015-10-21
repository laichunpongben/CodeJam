# Google Code Jam
# Code Jam Africa and Arabia 2011
# Qualification Round
# Problem A. Closing the Loop

class TestCase:
    def __init__(self):
        self.ropes = []
        
testCaseFile = open("ClosingTheLoop_A-small-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    count = -1
    for index, item in enumerate(lines):
        if (index > 0):
            if (index % 2 > 0 and count < n - 1):
                count += 1
                testCases[count] = TestCase()
                #testCases[count].rope = list(item)
            else: 
                testCases[count].rope = item.split(' ')

initialize_test_cases(lines)
