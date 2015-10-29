# Google Code Jam
# Google Code Jam 2015
# Round 1B
# Problem B. Noisy Neighbors

# Closed form solution O(1)

from math import ceil

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
        
        unhappiness_at_full = (r-1)*c+(c-1)*r
        max_n_at_zero = ceil(r*c/2)
        
        if (width == 1): 
            if ((r*c)%2==0): 
                if (n<=max_n_at_zero): return 0
                else: return 2*(n-max_n_at_zero)-1
            else: 
                if (n<=max_n_at_zero): return 0
                else: return 2*(n-max_n_at_zero)
        else: 
            min_n_at_minus_four = r*c - ceil((r-2)*(c-2)/2)
            if ((r*c)%2==0): 
                if (n<=max_n_at_zero): return 0
                elif (n<=max_n_at_zero+2): return 2*(n-max_n_at_zero)
                elif (n<min_n_at_minus_four): return 3*(n-max_n_at_zero)-2
                else: return unhappiness_at_full - 4*(r*c-n)
            else:
                min_n_at_minus_three = min_n_at_minus_four - (r+c-6)
                if (n<=max_n_at_zero): return 0
                elif (n<min_n_at_minus_three): return 3*(n-max_n_at_zero)
                elif (n<min_n_at_minus_four): return  unhappiness_at_full - 4*(r*c-min_n_at_minus_four) - 3*(min_n_at_minus_four-n)
                else: return unhappiness_at_full - 4*(r*c-n)

def initialize_test_cases(lines):
    global test_cases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                r = int(items[0])
                c = int(items[1])
                n = int(items[2])
                test_cases[index - 1] = TestCase(r, c, n)
                
def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x+1) + ': ' + str(test_cases[x].compute_min_unhappiness()))

test_case_file = open("NoisyNeighbors_B-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
