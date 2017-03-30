#!/usr/bin/env python
# Need solve time complexity

from __future__ import print_function

def count_recycled_pairs(a, b):
    count = 0
    for n in range(a, b):
        for m in range(n+1, b+1):
            if is_recycled_pair(n, m):
                count += 1
    return count

def count_digits(n):
    digits = [int(_) for _ in list(str(n))]
    return {digit: digits.count(digit) for digit in range(10)}

def is_recycled_pair(n, m):
    if len(str(n)) != len(str(m)):
        return False

    if count_digits(n) != count_digits(m):
        return False

    for i in range(len(str(m))):
        s = int(str(m)[i:] + str(m)[:i])
        if s == n:
            return True

    return False

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
