#!/usr/bin/env python

from __future__ import print_function
from functools import reduce

def split_candies(candies):
    assert isinstance(candies, list)
    xor = reduce(lambda x, y: x ^ y, candies)
    if xor == 0:
        return sum(candies) - min(candies)
    else:
        return 0

if __name__ == '__main__':
    import os

    samples = [
        [1,2,3,4,5],
        [3,5,6]
    ]

    for sample in samples:
        max_candy = split_candies(sample)
        if max_candy > 0:
            print(max_candy)
        else:
            print('NO')

    data_files = ['C-small-practice',
                  'C-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]
        test_cases = [[int(_) for _ in in_.split(' ')] for in_ in inputs[1::2]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                print(test_case)
                max_candy = split_candies(test_case)
                if max_candy > 0:
                    output_file.write('Case #{0}: {1}\n'.format(i, max_candy))
                else:
                    output_file.write('Case #{0}: {1}\n'.format(i, 'NO'))
                i += 1
