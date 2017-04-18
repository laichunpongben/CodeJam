#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Round 1A 2017
# Problem A. Alphabet Cake

# Solve all test sets

from __future__ import print_function

def make_cake(r, c, cake):
    assert isinstance(cake, list)

    filled_cake = []
    for row in cake:
        first_cell = '?'
        last_cell = '?'
        new_row = ''
        for cell in row:
            if cell != '?':
                last_cell = cell
                if first_cell == '?':
                    first_cell = cell
            new_row += last_cell
        new_row = new_row.replace('?', first_cell)
        filled_cake.append(new_row)

    filled_cake2 = []
    last_row = '?' * c
    first_row = '?' * c
    for row in filled_cake:
        if not '?' in row:
            last_row = row
            if '?' in first_row:
                first_row = row
        new_row = last_row
        filled_cake2.append(new_row)

    filled_cake2 = [first_row if '?' in row else row for row in filled_cake2]
    return filled_cake2

if __name__ == '__main__':
    import os

    samples = [
        (3, 3, ['G??', '?C?', '??J']),
        (3, 4, ['CODE', '????', '?JAM']),
        (2, 2, ['CA', 'KE'])
    ]

    for sample in samples:
        print(make_cake(*sample))

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        test_cases = []
        j = 0
        for _ in range(input_count):
            cake = []
            r, c = tuple([int(_) for _ in inputs[j].split(' ')])
            j += 1

            for _ in range(r):
                row = inputs[j]
                cake.append(row)
                j += 1
            test_cases.append((r, c, cake))

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                cake = make_cake(*test_case)
                output_file.write('Case #{0}:\n'.format(i))
                for row in cake:
                    output_file.write(row)
                    output_file.write('\n')

                i += 1
