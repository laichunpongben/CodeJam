# Google Code Jam
# Google Code Jam 2014
# Qualification Round 2014
# Problem A. Magic Trick

class TestCase:
    def __init__(self):
        self.answer1 = 0
        self.order1 = [[0 for x in range(4)] for x in range(4)]
        self.answer2 = 0
        self.order2 = [[0 for x in range(4)] for x in range(4)]
        
testCaseFile = open("MagicTrick_A-small-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    count = -1
    for index, item in enumerate(lines):
        if (index > 0):
            if (index % 10 == 1 and count < n - 1):
                count += 1
                testCases[count] = TestCase()
                testCases[count].answer1 = int(item)
            elif (index % 10 == 2): testCases[count].order1[0] = item.split(' ')
            elif (index % 10 == 3): testCases[count].order1[1] = item.split(' ')
            elif (index % 10 == 4): testCases[count].order1[2] = item.split(' ')
            elif (index % 10 == 5): testCases[count].order1[3] = item.split(' ')
            elif (index % 10 == 6): testCases[count].answer2 = int(item)
            elif (index % 10 == 7): testCases[count].order2[0] = item.split(' ')
            elif (index % 10 == 8): testCases[count].order2[1] = item.split(' ')
            elif (index % 10 == 9): testCases[count].order2[2] = item.split(' ')
            elif (index % 10 == 0): testCases[count].order2[3] = item.split(' ')
            
            
def determine_card(testCase):
    cards1 = testCase.order1[testCase.answer1 - 1]
    cards2 = testCase.order2[testCase.answer2 - 1]
    return set(cards1).intersection(cards2)
    
def get_result(cards):
    countCards = len(cards)
    if (countCards == 1): return cards.pop()
    elif (countCards == 0): return "Volunteer cheated!"
    else: return "Bad magician!"
    
def print_all_results():
    for x in range(len(testCases)):
        print('Case #' + str(x + 1) + ': ' + str(get_result(determine_card(testCases[x]))))
            
initialize_test_cases(lines)
print_all_results()
