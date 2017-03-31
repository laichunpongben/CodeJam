#!/usr/bin/env python
# Need solve time complexity

from __future__ import print_function
from collections import deque

def count_fair_and_square_numbers(a, b):
    count = 0
    n = a
    while n <= b:
        if is_fair_and_square(n):
            count += 1
        n += 1
    return count

def is_fair_and_square(n):
    assert isinstance(n, int) or isinstance(n, long)
    if is_palindrome(n):
        if is_square(n):
            return is_palindrome(int(n ** 0.5))
        else:
            return False
    else:
        return False

def is_square(n):
    assert isinstance(n, int) or isinstance(n, long)

    if 0 <= n <= 1:
        return True

    x = n // 2
    seen = set([x])
    while x ** 2 != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True

def is_palindrome(n):
    assert isinstance(n, int) or isinstance(n, long)
    dq = deque(str(n))
    dq.reverse()
    n_ = int(''.join(dq))
    return n == n_

if __name__ == '__main__':
    import os

    print(is_square(152415789666209426002111556165263283035677489))

    samples = [
        (1, 4),
        (10, 120),
        (100, 1000)
    ]

    for sample in samples:
        print(count_fair_and_square_numbers(*sample))

    data_files = ['C-small-practice', 'C-large-practice-1', 'C-large-practice-2']
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
                output_file.write('Case #{0}: {1}\n'.format(i, count_fair_and_square_numbers(a, b)))
                i += 1
