#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2014
# Qualification Round 2014
# Problem A. Magic Trick

# Solved

class TestCase:
    def __init__(self):
        self.answer1 = 0
        self.order1 = [[0 for x in range(4)] for x in range(4)]
        self.answer2 = 0
        self.order2 = [[0 for x in range(4)] for x in range(4)]

    def determine_card(self):
        cards1 = self.order1[self.answer1 - 1]
        cards2 = self.order2[self.answer2 - 1]
        return set(cards1).intersection(cards2)

def initialize_test_cases(lines):
    global test_cases
    count = -1
    for index, item in enumerate(lines):
        if (index > 0):
            if (index % 10 == 1 and count < n - 1):
                count += 1
                test_cases[count] = TestCase()
                test_cases[count].answer1 = int(item)
            elif (index % 10 == 2): test_cases[count].order1[0] = item.split(' ')
            elif (index % 10 == 3): test_cases[count].order1[1] = item.split(' ')
            elif (index % 10 == 4): test_cases[count].order1[2] = item.split(' ')
            elif (index % 10 == 5): test_cases[count].order1[3] = item.split(' ')
            elif (index % 10 == 6): test_cases[count].answer2 = int(item)
            elif (index % 10 == 7): test_cases[count].order2[0] = item.split(' ')
            elif (index % 10 == 8): test_cases[count].order2[1] = item.split(' ')
            elif (index % 10 == 9): test_cases[count].order2[2] = item.split(' ')
            elif (index % 10 == 0): test_cases[count].order2[3] = item.split(' ')

def get_result(cards):
    count_cards = len(cards)
    if (count_cards == 1): return cards.pop()
    elif (count_cards == 0): return "Volunteer cheated!"
    else: return "Bad magician!"

def print_all_results():
    for x in range(len(test_cases)):
        print('Case #' + str(x + 1) + ': ' + str(get_result(determine_card(test_cases[x]))))

test_case_file = open("MagicTrick_A-small-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
