#!/usr/bin/env python

# Google Code Jam
# Kickstart 2017
# Kickstart Practice Round 2017
# Problem C. Sherlock and Parentheses

# Solved all test sets

from __future__ import print_function, division

def solve(l, r):
    n = min(l, r)
    return int(n * (n+1) / 2)

if __name__ == '__main__':
    import os

    samples = [
        (1, 0),
        (1, 1),
        (3, 2)
    ]

    for sample in samples:
        print(solve(*sample))

    data_files = ['C-small-practice',
                  'C-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for line in inputs:
                l, r = tuple([int(_) for _ in line.split(' ')])
                y = solve(l, r)
                output_file.write('Case #{0}: {1}\n'.format(i, y))

                i += 1
