#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2013
# Qualification Round 2013
# Problem C. Fair and Square

# Solved all test sets

from __future__ import print_function
import math
from bisect import bisect_left
import itertools

def build_fair_and_squares(a, b):
    assert isinstance(a, (int, long))
    assert isinstance(b, (int, long))

    def func0(i):
        assert i >= 1
        patterns = []
        zero_one_generator = itertools.product(('0', '1'), repeat=i-1)
        zero_one_product = ['1' + ''.join(_) for _ in zero_one_generator]
        patterns.extend(zero_one_product)
        patterns.append('2' + '0' * (i-1))
        fair_and_squares = [int(i + i[::-1]) ** 2 for i in patterns]
        return fair_and_squares

    def func1(i):
        assert i >= 1
        if i == 1:
            return []
        patterns = []
        zero_one_generator = itertools.product(('0', '1'), repeat=i-2)
        zero_one_product = ['1' + ''.join(_) + str(x) for _ in zero_one_generator for x in range(3)]
        patterns.extend(zero_one_product)
        patterns.extend(['2' + '0' * (i-2) + str(x) for x in range(3)])
        fair_and_squares = [int(i + i[-2::-1]) ** 2 for i in patterns]
        return fair_and_squares

    fair_and_squares = [1, 4, 9]

    length_a = int(math.ceil(float(len(str(a))) / 4))
    if is_power(b, 10):
        length_b = int(math.ceil(float(len(str(b)) - 1) / 4))
    else:
        length_b = int(math.ceil(float(len(str(b))) / 4))

    i = 1

    while i <= length_b:
        for f in [func0, func1]:
            fns = f(i)
            fair_and_squares.extend(fns)
        i += 1

    fair_and_squares = sorted([_ for _ in fair_and_squares if a <= _ <= b and is_palindrome(_)])

    return fair_and_squares

def is_palindrome(n):
    return str(n) == str(n)[::-1]

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

    palindromes = sorted([_ for _ in list(set(palindromes)) if a <= _ <= b])
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
        fair_and_squares = build_fair_and_squares(1, max_range)
        for _ in fair_and_squares:
            print(_)
        print(len(fair_and_squares))

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for in_ in input_ranges:
                a, b = in_
                print(a, b)
                output_file.write('Case #{0}: {1}\n'.format(i, count_sorted(fair_and_squares, a, b)))
                i += 1
