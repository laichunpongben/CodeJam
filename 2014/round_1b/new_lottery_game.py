#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2014
# Round 2 2014
# Problem B. New Lottery Game

# Solved small set

from __future__ import print_function
import itertools

def count_winning_pairs(a, b, k):
    permutations = itertools.product(range(a), range(b))
    count = 0
    for _ in permutations:
        if _[0] & _[1] < k:
            count += 1
    return count

if __name__ == '__main__':
    import os

    samples = [
        (3,4,2),
        (4,5,2),
        (7,8,5),
        (45,56,35),
        (103,143,88)
    ]

    for sample in samples:
        print(count_winning_pairs(*sample))

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
                a, b, k = tuple([int(_) for _ in in_.split(' ')])
                print(a, b, k)
                output_file.write('Case #{0}: {1}\n'.format(i, count_winning_pairs(a, b, k)))
                i += 1
