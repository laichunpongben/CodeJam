#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Qualification Round 2017
# Problem A. Oversized Pancake Flipper

# Solved all test sets

from __future__ import print_function
import itertools
from functools import reduce
import operator
import sys

def build_sk_dict(max_s_length):
    sk_dict = {}
    for s in range(2, max_s_length + 1):
        sk_dict[s] = {}
        for k in range(2, s + 1):
            sk_dict[s][k] = []
            xors = [int('1' * k, 2) * (2 ** j) for j in range(s - k + 1)]
            for r in range(s - k + 2):
                combo = itertools.combinations(xors, r)
                for c in combo:
                    zxor = reduce(operator.xor, c, 0)
                    sk_dict[s][k] = r
                    print(s, k, zxor, r, c)
    return sk_dict

def s_to_digits(s):
    return s.replace('+', '0').replace('-', '1')

def get_xors(s, k):
    return sorted([int('1' * k, 2) * (2 ** j) for j in range(len(s) - k + 1)], reverse=True)

def calc_min_flip_step(s, k):
    assert isinstance(k, int)

    digits = s_to_digits(s)

    if not '1' in digits:
        return 0

    xors = get_xors(s, k)

    min_flip_step = 0
    for i in range(len(s) - k + 1):
        if digits[i] == '1':
            min_flip_step += 1
            flipped = int(digits, 2) ^ xors[i]
            digits = format(flipped, '#0{0}b'.format(len(s)+2))[2:]

    if '1' in digits:
        return sys.maxint

    assert min_flip_step > 0

    return min_flip_step

if __name__ == '__main__':
    import os

    samples = [
        ('++', 2),
        ('+++', 2),
        ('++++', 2),
        ('+++++', 2),
        ('++++++', 2),
        ('+++++++', 2),
        ('+'*10, 5),
        ('++++', 3),
        ('+++++', 3),
        ('+++++', 4),
        ('+'*100, 3),
        ('---+-++-', 3),
        ('+++++', 4),
        ('-+-+-', 4),
        ('---+-++++', 3),
        ('---+-++++', 2),
        ('---+-++++', 4),
    ]

    for sample in samples:
        min_flip_step = calc_min_flip_step(*sample)
        if min_flip_step == sys.maxint:
            print('IMPOSSIBLE')
        else:
            print(min_flip_step)

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
                line = tuple([_ for _ in in_.split(' ')])
                s = line[0]
                k = int(line[1])
                min_flip_step = calc_min_flip_step(s, k)
                if min_flip_step == sys.maxint:
                    output_file.write('Case #{0}: IMPOSSIBLE\n'.format(i))
                else:
                    output_file.write('Case #{0}: {1}\n'.format(i, min_flip_step))
                i += 1
