#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Round 1B 2017
# Problem A. Steed 2: Cruise Control

# Solved all test sets

from __future__ import print_function, division
import sys

def calc_time(d, k, s):
    return (d-k)/s

def calc_annie_speed(d, n, horses):
    assert isinstance(horses, list)

    max_t = 0.0
    for horse in horses:
        t = calc_time(d, horse[0], horse[1])
        if t > max_t:
            max_t = t

    return d / max_t

if __name__ == '__main__':
    import os

    samples = [
        (2525, 1, [(2400, 5)]),
        (300, 2, [(120, 60), (60, 90)]),
        (100, 2, [(80, 100), (70, 10)])
    ]

    for sample in samples:
        print(calc_annie_speed(*sample))

    data_files = ['A-small-attempt0',
                  'A-large']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        test_cases = []
        j = 0
        for _ in range(input_count):
            horses = []
            d, n = tuple([int(_) for _ in inputs[j].split(' ')])
            j += 1

            for _ in range(n):
                horse = tuple([int(_) for _ in inputs[j].split(' ')])
                horses.append(horse)
                j += 1
            test_cases.append((d, n, horses))

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                t = calc_annie_speed(*test_case)
                output_file.write('Case #{0}: {1:0.6f}\n'.format(i, t))

                i += 1
