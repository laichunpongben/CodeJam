#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2013
# Round 1A 2013
# Problem A. Bullseye

# Solved all test sets

from __future__ import print_function, division

def calc_paint(n, r):
    return n * (2 * n + 2 * r - 1)

def calc_max_n(r, t):
    assert isinstance(r, (int, long))
    assert isinstance(t, (int, long))

    high = 2 * 10 ** 18
    low = 0
    mid = int((high + low) / 2)

    while low < high:
        mid = int((high + low) / 2)
        paint = calc_paint(mid, r)
        if paint == t:
            return mid
        elif paint > t and mid < high:
            high = max(mid - 1, low)
        elif paint < t and low < mid:
            low = min(mid, high)
        else:
            break

    assert high - low <= 1

    if calc_paint(high, r) > t:
        return int(low)
    else:
        return int(high)

if __name__ == '__main__':
    import os

    samples = [
        (1, 9),
        (1, 10),
        (3, 40),
        (1, 1000000000000000000),
        (10000000000000000, 1000000000000000000),
        (138, 844),
        (21, 197),
        (82, 866)
    ]

    for sample in samples:
        print(calc_max_n(*sample))

    data_files = ['A-small-practice', 'A-large-practice']
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
                print('Case', i)
                r, t = tuple([int(_) for _ in in_.split(' ')])
                output_file.write('Case #{0}: {1}\n'.format(i, calc_max_n(r, t)))

                i += 1
