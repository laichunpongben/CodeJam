# Google Code Jam
# Google Code Jam 2013
# Qualification Round 2013
# Problem A. Tic-Tac-Toe-Tomek

# Solved

class TestCase:
    def __init__(self):
        self.board = [0 for x in range(4)]
        
    def get_orders(self):
        orders = [0 for x in range(10)]
        orders[0] = self.board[0]
        orders[1] = self.board[1]
        orders[2] = self.board[2]
        orders[3] = self.board[3]
        orders[4] = list(self.board[x][0] for x in range(4))
        orders[5] = list(self.board[x][1] for x in range(4))
        orders[6] = list(self.board[x][2] for x in range(4))
        orders[7] = list(self.board[x][3] for x in range(4))
        orders[8] = list(self.board[x][x] for x in range(4))
        orders[9] = list(self.board[x][3 - x] for x in range(4))
        return orders
        
    def determine_game_state(self):
        orders = self.get_orders()
        count_dot = 0
        for order in orders:
            if (order.count('X') == 4): return 'X won'
            elif (order.count('X') == 3 and order.count('T') == 1): return 'X won'
            elif (order.count('O') == 4): return 'O won'
            elif (order.count('O') == 3 and order.count('T') == 1): return 'O won'
            count_dot += order.count('.')
        if (count_dot == 0): return 'Draw'
        else: return 'Game has not completed'

def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if (index > 0):
            if (index % 5 == 1 and count < n - 1):
                count += 1
                test_cases[count] = TestCase()
                test_cases[count].board[0] = list(item)
            elif (index % 5 == 2): test_cases[count].board[1] = list(item)
            elif (index % 5 == 3): test_cases[count].board[2] = list(item)
            elif (index % 5 == 4): test_cases[count].board[3] = list(item)
            else: continue

def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x + 1) + ': ' + determine_game_state(test_cases[x]))

test_case_file = open("TicTacToeTomek_A-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
