#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2012
# Qualification Round 2012
# Problem C. Recycled Numbers

# Solved all test sets
# Time complexity: O(NlogN)

from __future__ import print_function

def count_recycled_pairs(a, b):
    recycled_pairs = []
    for n in range(a, b):
        for i in range(1, len(str(n))):
            m = int(str(n)[i:] + str(n)[:i])
            if n < m <= b:
                recycled_pairs.append((n, m))
    recycled_pairs = list(set(recycled_pairs))
    return len(recycled_pairs)

if __name__ == '__main__':
    import os

    samples = [
        (1, 9),
        (10, 40),
        (100, 500),
        (1111, 2222)
    ]

    for sample in samples:
        print(count_recycled_pairs(*sample))

    data_files = ['C-small-practice', 'C-large-practice']
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
                a, b = tuple([int(_) for _ in in_.split(' ')])
                print(a, b)
                output_file.write('Case #{0}: {1}\n'.format(i, count_recycled_pairs(a, b)))
                i += 1
