# Google Code Jam
# Google APAC 2016 University Graduates Test
# Practice Round APAC test 2016 
# Problem C. Moist

class TestCase:
    def __init__(self):
        self.cards = []
        
testCaseFile = open("Moist_C-small-practice-1.in", "r")
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
                testCases[count].cards.extend([item])

def insertionSortAndCount(mylist):
    count = 0
    for index in range(1, len(mylist)):
        currentValue = mylist[index]
        position = index

        if (position > 0 and mylist[position - 1] > currentValue): count += 1
        while position > 0 and mylist[position - 1] > currentValue:
            mylist[position] = mylist[position - 1]
            position = position - 1
    
        mylist[position] = currentValue
    return count

def print_all_results():
    for x in range(len(testCases)):
        #print(testCases[x].cards)
        count = insertionSortAndCount(testCases[x].cards)
        print('Case #' + str(x + 1) + ': ' + str(count))

initialize_test_cases(lines)
print_all_results()
