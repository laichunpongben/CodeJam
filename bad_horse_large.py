# Google Code Jam
# Google APAC 2016 University Graduates Test
# Practice Round APAC test 2016 
# Problem A. Bad Horse

# Solved

from random import shuffle

class TestCase:
    def __init__(self):
        self.players = set()
        self.trouble_pairs = []
        
    def is_safe_set_exist(self):
        set1 = set()
        set2 = set()
        unsolved_pairs = self.trouble_pairs
        count = 0
        
        shuffle(unsolved_pairs)
        set1.add(unsolved_pairs[0][0])
        set2.add(unsolved_pairs[0][1])
        unsolved_pairs.remove(unsolved_pairs[0])
        unsolved_pairs.sort()
        
        while (len(unsolved_pairs) > 0 and count < 100):
            count += 1
            for pair in unsolved_pairs:
                if ((pair[0] in set1 and pair[1] not in set1) or (pair[1] in set2 and pair[0] not in set2)):
                    set1.add(pair[0])
                    set2.add(pair[1])
                    unsolved_pairs.remove(pair)
                elif ((pair[0] in set2 and pair[1] not in set2) or (pair[1] in set1 and pair[0] not in set1)):
                    set1.add(pair[1])
                    set2.add(pair[0])
                    unsolved_pairs.remove(pair)
                elif ((pair[0] in set1 and pair[1] in set1) or (pair[0] in set2 and pair[1] in set2)):
                    return False
    
        return True

def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if index > 0: 
            if item.isdigit(): 
                count += 1
                test_cases[count] = TestCase()
            else: 
                p = item.split(' ')
                if (len(p) > 1):
                    test_cases[count].players.add(p[0])
                    test_cases[count].players.add(p[1])
                    test_cases[count].trouble_pairs.append(p)
          
def print_all_results():
    for x in range(len(test_cases)):
        if test_cases[x].is_safe_set_exist(): print('Case #' + str(x + 1) + ': Yes')
        else: print('Case #' + str(x + 1) + ': No')

test_case_file = open("BadHorse_A-small-practice-2.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
