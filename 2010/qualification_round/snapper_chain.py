#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2010
# Qualification Round 2010
# Problem A. Snapper Chain

# Solved all test sets

from __future__ import print_function

def get_status(n, k):
    if k % (2 ** n) == 2 ** n - 1:
        return 'ON'
    else:
        return 'OFF'

if __name__ == '__main__':
    import os

    samples = [
        (1, 0),
        (1, 1),
        (4, 0),
        (4, 47),
        (1, 2),
        (1, 3)
    ]

    for sample in samples:
        print(get_status(*sample))

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for in_ in inputs:
                n, k = tuple([int(_) for _ in in_.split(' ')])
                output_file.write('Case #{0}: {1}\n'.format(i, get_status(n, k)))

                i += 1
