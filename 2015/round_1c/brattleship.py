#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2015
# Round 1C 2015
# Problem A. Brattleship

# Solved all test sets

from __future__ import print_function, division
import math

def get_score(r, c, w):
    if r == 1:
        if w in [1, c]:
            return c
        else:
            return min(max(int(math.ceil(c/w)) + w - 1, w + 1), c)
    else:
        if w == 1:
            return r * c
        elif w == c:
            return r + c - 1
        else:
            return (r-1) * int(c/w) + min(max(int(math.ceil(c/w)) + w - 1, w + 1), c)

if __name__ == '__main__':
    import os

    samples = [
        (1, 4, 2),
        (1, 7, 7),
        (2, 5, 1)
    ]

    for sample in samples:
        print(get_score(*sample))

    data_files = ['A-small-practice',
                  'A-large-practice']
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
                line = tuple([int(_) for _ in in_.split(' ')])
                r, c, w = line
                output_file.write('Case #{0}: {1}\n'.format(i, get_score(r, c, w)))
                i += 1
