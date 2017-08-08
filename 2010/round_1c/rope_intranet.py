#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2010
# Round 1C 2010
# Problem A. Rope Intranet

# Solved all test sets

from __future__ import print_function
import itertools

def count_intersections(ropes):
    assert isinstance(ropes, list)

    combo = itertools.combinations(ropes, 2)
    intersection = 0
    for c in combo:
        if (c[0][0] < c[1][0] and c[0][1] > c[1][1]) or \
           (c[0][0] > c[1][0] and c[0][1] < c[1][1]):
           intersection += 1
    return intersection

if __name__ == '__main__':
    import os

    samples = [
        [
            (1,10),
            (5,5),
            (7,7)
        ],
        [
            (1,1),
            (2,2)
        ]
    ]

    for sample in samples:
        print(count_intersections(sample))

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
            ropes = []
            n = int(inputs[j])
            j += 1

            for _ in range(n):
                rope = tuple([int(_) for _ in inputs[j].split(' ')])
                ropes.append(rope)
                j += 1
            test_cases.append(ropes)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                output_file.write('Case #{0}: {1}\n'.format(i, count_intersections(test_case)))

                i += 1
