#!/usr/bin/env python

# Google Code Jam
# Kickstart 2017
# Kickstart Practice Round 2017
# Problem A. Country Leader

# Solved all test sets

from __future__ import print_function

def count_letters(name):
    letters = list(set(name))
    if ' ' in letters:
        letters.remove(' ')
    return len(letters)

def solve(countries):
    countries = sorted(countries, key=lambda x: (-count_letters(x), x))
    return countries[0]

if __name__ == '__main__':
    import os

    samples = [
        ['ADAM', 'BOB', 'JOHNSON'],
        ['A AB C', 'DEF']
    ]

    for sample in samples:
        print(solve(sample))

    data_files = ['A-small-practice',
                  'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        test_cases = []
        j = 0
        for _ in range(input_count):
            countries = []
            n = int(inputs[j])
            j += 1

            for _ in range(n):
                countries.append(inputs[j])
                j += 1
            test_cases.append(countries)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                country = solve(test_case)
                output_file.write('Case #{0}: {1}\n'.format(i, country))

                i += 1
