#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2010
# Qualification Round 2010
# Problem B. Fair Warning

# Solved all test sets

from __future__ import print_function
from fractions import gcd
from functools import reduce

def get_y(ts):
    ts = sorted(ts)
    y = ts[0]
    l0 = [abs(x - y) for x in ts]
    g = reduce(gcd, l0)
    if y % g == 0:
        return 0
    else:
        return g - (y % g)

if __name__ == '__main__':
    import os

    samples = [
        [26000000, 11000000, 6000000],
        [1, 10, 11],
        [800000000000000000001, 900000000000000000001]
    ]

    for sample in samples:
        print(get_y(sample))

    data_files = ['B-small-practice', 'B-large-practice']
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
                ts = [int(_) for _ in in_.split(' ')]
                ts = ts[1:]
                output_file.write('Case #{0}: {1}\n'.format(i, get_y(ts)))

                i += 1
