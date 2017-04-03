# Google Code Jam
# Google Code Jam 2015
# Round 1A
# Problem A. Mushroom Monster

# Solved

class TestCase:
    def __init__(self):
        self.mushrooms = []
        
    def compute_method1_min(self):
        mushroom_eaten = 0
        for x in range(len(self.mushrooms) - 1):
            mushroom_eaten += max(self.mushrooms[x] - self.mushrooms[x+1], 0)
        return mushroom_eaten
    
    def compute_method2_rate(self):
        rate = 0
        for x in range(len(self.mushrooms) - 1):
            rate = max(self.mushrooms[x] - self.mushrooms[x+1], rate)
        return rate
        
    def compute_method2_min(self):
        mushroom_eaten = 0
        rate = self.compute_method2_rate()
        for x in range(len(self.mushrooms) - 1):
            mushroom_eaten += min(self.mushrooms[x], rate)
        return mushroom_eaten

def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if (index % 2 > 0): 
                count += 1
                if (count < n):
                    test_cases[count] = TestCase()
                    period = int(item)
                    test_cases[count].mushrooms = [0 for x in range(period)]
            else: 
                p = item.split(' ')
                if (len(p) > 0):
                    for x in range(len(test_cases[count].mushrooms)):
                        test_cases[count].mushrooms[x] = int(p[x])

def print_all_results():
    for x in range(len(test_cases)):
        y = test_cases[x].compute_method1_min()
        z = test_cases[x].compute_method2_min()
        print('Case #' + str(x+1) + ': ' + str(y) + ' ' + str(z))

testCaseFile = open("MushroomMonster_A-large-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
