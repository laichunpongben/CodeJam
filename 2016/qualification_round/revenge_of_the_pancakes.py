#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2016
# Qualification Round 2016
# Problem B. Revenge of the Pancakes

# Solved all test sets

from __future__ import print_function

def calc_min_flip_step(s):
    grouped_height = 1 + s.count('-+') + s.count('+-')
    if s.endswith('-'):
        return grouped_height
    else:
        return grouped_height - 1

if __name__ == '__main__':
    import os

    samples = [
        '-',
        '-+',
        '+-',
        '+++',
        '--+-'
    ]

    for sample in samples:
        print(calc_min_flip_step(sample))

    data_files = ['B-small-practice',
                  'B-large-practice']
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
                output_file.write('Case #{0}: {1}\n'.format(i, calc_min_flip_step(in_)))
                i += 1
