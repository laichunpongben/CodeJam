# Google Code Jam
# Google Code Jam 2014
# Qualification Round 2014
# Problem A. Tic-Tac-Toe-Tomek

class TestCase:
    def __init__(self):
        self.board = [0 for x in range(4)]
        
testCaseFile = open("TicTacToeTomek_A-large-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

def initialize_test_cases(lines):
    global testCases
    count = -1
    for index, item in enumerate(lines):
        if (index > 0):
            if (index % 5 == 1 and count < n - 1):
                count += 1
                testCases[count] = TestCase()
                testCases[count].board[0] = list(item)
            elif (index % 5 == 2): testCases[count].board[1] = list(item)
            elif (index % 5 == 3): testCases[count].board[2] = list(item)
            elif (index % 5 == 4): testCases[count].board[3] = list(item)
            else: continue

def get_orders(testCase):
    orders = [0 for x in range(10)]
    orders[0] = testCase.board[0]
    orders[1] = testCase.board[1]
    orders[2] = testCase.board[2]
    orders[3] = testCase.board[3]
    orders[4] = list(testCase.board[x][0] for x in range(4))
    orders[5] = list(testCase.board[x][1] for x in range(4))
    orders[6] = list(testCase.board[x][2] for x in range(4))
    orders[7] = list(testCase.board[x][3] for x in range(4))
    orders[8] = list(testCase.board[x][x] for x in range(4))
    orders[9] = list(testCase.board[x][3 - x] for x in range(4))
    return orders

def determine_game_state(testCase):
    orders = get_orders(testCase)
    countDot = 0
    for order in orders:
        if (order.count('X') == 4): return 'X won'
        elif (order.count('X') == 3 and order.count('T') == 1): return 'X won'
        elif (order.count('O') == 4): return 'O won'
        elif (order.count('O') == 3 and order.count('T') == 1): return 'O won'
        countDot += order.count('.')
    if (countDot == 0): return 'Draw'
    else: return 'Game has not completed'

def print_all_results():
    for x in range(len(testCases)):
        #print(get_orders(testCases[x]))
        print('Case #' + str(x + 1) + ': ' + determine_game_state(testCases[x]))

initialize_test_cases(lines)
print_all_results()
