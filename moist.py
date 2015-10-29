# Google Code Jam
# Google APAC 2016 University Graduates Test
# Practice Round APAC test 2016 
# Problem C. Moist

# Unsolved

class TestCase:
    def __init__(self):
        self.cards = []

def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if item.isdigit(): 
                count += 1
                test_cases[count] = TestCase()
            else: 
                test_cases[count].cards.extend([item])

def insertion_sort_and_count(mylist):
    count = 0
    for index in range(1, len(mylist)):
        current_value = mylist[index]
        position = index

        if (position > 0 and mylist[position - 1] > current_value): count += 1
        while position > 0 and mylist[position - 1] > current_value:
            mylist[position] = mylist[position - 1]
            position = position - 1
    
        mylist[position] = current_value
    return count

def print_all_results():
    for x in range(len(test_cases)):
        count = insertion_sort_and_count(test_cases[x].cards)
        print('Case #' + str(x + 1) + ': ' + str(count))

testCaseFile = open("Moist_C-small-practice-1.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
