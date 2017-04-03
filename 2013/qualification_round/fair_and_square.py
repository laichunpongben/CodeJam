#!/usr/bin/env python
# Need solve time complexity

from __future__ import print_function
import math
from bisect import bisect_left

def get_fair_and_squares(a, b):
    assert isinstance(a, (int, long))
    assert isinstance(b, (int, long))

    p = build_palindromes(a, b)
    p2 = [_ ** 2 for _ in build_palindromes(int(a ** 0.5),
          int(math.ceil(b ** 0.5)))
          if a <= _ ** 2 <= b]

    return sorted(list(set(p).intersection(set(p2))))

def build_palindromes(a, b):
    assert isinstance(a, (int, long))
    assert isinstance(b, (int, long))

    def func0(i):
        return str(i)[::-1] + str(i)

    def func1(i):
        return str(i)[:0:-1] + str(i)

    def func2(i):
        return str(i) + str(i)[::-1]

    def func3(i):
        return str(i) + str(i)[-2::-1]

    palindromes = []

    length_a = int(math.ceil(float(len(str(a))) / 2))
    if is_power(b, 10):
        length_b = int(math.ceil(float(len(str(b)) - 1) / 2))
    else:
        length_b = int(math.ceil(float(len(str(b))) / 2))

    i = 10 ** (length_a - 1)
    while len(str(i)) <= length_b:
        for f in [func0, func1, func2, func3]:
            palindrome = f(i)
            if int(palindrome[0]) > 0:
                palindromes.append(int(palindrome))
        i += 1

    palindromes = [_ for _ in list(set(palindromes)) if a <= _ <= b]
    return palindromes

def is_power(num, base):
    if base == 1 and num != 1: return False
    if base == 1 and num == 1: return True
    if base == 0 and num != 1: return False
    power = int (math.log (num, base) + 0.5)
    return base ** power == num

def count_sorted(mylist, a, b):
    count = 0
    if mylist:
        position = bisect_left(mylist, a)
        for item in mylist[position:]:
            if a <= item <= b:
                count += 1
            elif item > b:
                break
        return count
    else:
        return 0

if __name__ == '__main__':
    import os

    samples = [
        (1, 4),
        (10, 120),
        (100, 1000)
    ]

    for sample in samples:
        a, b = sample
        fair_and_squares = get_fair_and_squares(a, b)
        print(fair_and_squares)
        print(count_sorted(fair_and_squares, a, b))

    data_files = ['C-small-practice',
                  'C-large-practice-1',
                  'C-large-practice-2']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]
        input_ranges = [tuple([int(_) for _ in in_.split(' ')]) for in_ in inputs]
        max_range = max(input_ranges, key=lambda x: x[1])[1]
        print(max_range)
        fair_and_squares = get_fair_and_squares(1, max_range)
        print(fair_and_squares)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for in_ in input_ranges:
                a, b = in_
                print(a, b)
                output_file.write('Case #{0}: {1}\n'.format(i, count_sorted(fair_and_squares, a, b)))
                i += 1
