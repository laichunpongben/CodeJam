#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Qualification Round 2017
# Problem B. Tidy Numbers

# Solved all test sets

from __future__ import print_function
import math

def is_tidy(n):
    s = str(n)
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def get_last_tidy_number(n):
    assert isinstance(n, (int, long))

    if is_tidy(n):
        return n

    digits = list(str(n))
    max_digit = max([int(_) for _ in digits])

    if max_digit == 1:
        return int('9' * (len(str(n))-1))

    for i in range(len(digits)):
        digit = int(digits[i])
        min_tidy = int(''.join(digits[:i] + [str(digit)] * (len(digits) - i)))
        if min_tidy > n:
            result = int(''.join(digits[:i] + [str(digit-1)] + ['9'] * (len(digits) - i - 1)))
            return result
        else:
            continue

    return 0

if __name__ == '__main__':
    import os

    samples = [
        132,
        1000,
        7,
        111111111111111110,
        1000000000000000000000000,
        999999999999999998,
        465456494618904980,
        498089465064560150,
        999989777790000030,
        100000000000564656,
        128887498984665464,
        132132121321561101,
        999999999999999999,
        987654321012345679,
        123456789999999998
    ]

    for sample in samples:
        print(get_last_tidy_number(sample))

    data_files = ['B-small-practice',
                  'B-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [int(line.replace('\n', '')) for line in lines[1:]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for in_ in inputs:
                n = int(in_)
                output_file.write('Case #{0}: {1}\n'.format(i, get_last_tidy_number(n)))
                i += 1
