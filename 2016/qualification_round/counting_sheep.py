#!/usr/bin/env python

from __future__ import print_function

ALL_NUMS = set(range(0,10))
VERY_LARGE_INT = 1000

def get_digits(n):
    if isinstance(n, int):
        digits = list(str(n))
        return set([int(_) for _ in digits])
    else:
        raise ValueError

def get_last_num(n):
    seen_num = set()
    i = 1
    while True:
        digits = get_digits(n*i)
        seen_num = seen_num.union(digits)
        if seen_num == ALL_NUMS:
            return n*i
        elif i > VERY_LARGE_INT:
            return 'INSOMNIA'
        else:
            i = i + 1

if __name__ == '__main__':
    samples = [0, 1, 2, 11, 1692]
    for _ in samples:
        print(get_last_num(_))

    with open('A-large-practice.in', 'r') as input_file:
        lines = input_file.readlines()
    input_count = int(lines[0].replace('\n' ,''))
    inputs = [int(line.replace('\n', '')) for line in lines[1:]]

    i = 1
    with open('A-large-practice.out', 'w') as output_file:
        for in_ in inputs:
            output_file.write('Case #{0}: {1}\n'.format(i, get_last_num(in_)))
            i += 1
