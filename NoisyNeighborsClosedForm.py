# Google Code Jam
# Google Code Jam 2015
# Round 1B
# Problem B. Noisy Neighbors

# Closed form solution O(1)

from math import ceil

testCaseFile = open("NoisyNeighbors_B-large-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

class TestCase:
    def __init__(self, r, c, n):
        self.row = r
        self.column = c
        self.tenant = n
        
    def compute_min_unhappiness(self):
        r = self.row
        c = self.column
        n = self.tenant
        width = int(min(r,c))
        
        unhappinessAtFull = (r-1)*c+(c-1)*r
        maxNAtZero = ceil(r*c/2)
        
        if (width == 1): 
            if ((r*c)%2==0): 
                if (n<=maxNAtZero): return 0
                else: return 2*(n-maxNAtZero)-1
            else: 
                if (n<=maxNAtZero): return 0
                else: return 2*(n-maxNAtZero)
        else: 
            minNAtMinusFour = r*c - ceil((r-2)*(c-2)/2)
            if ((r*c)%2==0): 
                if (n<=maxNAtZero): return 0
                elif (n<=maxNAtZero+2): return 2*(n-maxNAtZero)
                elif (n<minNAtMinusFour): return 3*(n-maxNAtZero)-2
                else: return unhappinessAtFull - 4*(r*c-n)
            else:
                minNAtMinusThree = minNAtMinusFour - (r+c-6)
                if (n<=maxNAtZero): return 0
                elif (n<minNAtMinusThree): return 3*(n-maxNAtZero)
                elif (n<minNAtMinusFour): return  unhappinessAtFull - 4*(r*c-minNAtMinusFour) - 3*(minNAtMinusFour-n)
                else: return unhappinessAtFull - 4*(r*c-n)

def initialize_test_cases(lines):
    global testCases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                r = int(items[0])
                c = int(items[1])
                n = int(items[2])
                testCases[index - 1] = TestCase(r, c, n)
                
def print_all_results():
    for x in range(len(testCases)):
        print('Case #' + str(x+1) + ': ' + str(testCases[x].compute_min_unhappiness()))

initialize_test_cases(lines)
print_all_results()
