#!/usr/bin/env python
# Need solve time complexity

from __future__ import print_function
import math

def count_fair_and_square_numbers(a, b):
    palindromes = build_palindromes(a, b)
    print(palindromes)
    palindrome_squares = [_ ** 2 for _ in build_palindromes(int(a ** 0.5),
                          int(math.ceil(b ** 0.5)))
                          if a <= _ ** 2 <= b]
    fair_and_squares = list(set(palindromes).intersection(set(palindrome_squares)))
    return len(fair_and_squares)

def build_palindromes(a, b):
    def func0(i):
        return str(i)[::-1] + str(i)

    def func1(i):
        print('*******', str(i)[1::-1], str(i))
        return str(i)[1::-1] + str(i)

    def func2(i):
        return str(i) + str(i)[::-1]

    def func3(i):
        print('########', str(i), str(i)[:-1:-1])
        return str(i) + str(i)[:-1:-1]


    palindromes = []

    length_a = int(math.ceil(float(len(str(a))) / 2))
    length_b = int(math.ceil(float(len(str(b))) / 2))
    i = 10 ** (length_a - 1)
    print('i', i)
    print('length_b', length_b)
    while len(str(i)) <= length_b:
        for f in [func0, func1, func2, func3]:
            palindrome = f(i)
            print('p', palindrome)
            if int(palindrome[0]) > 0:
                # print('q', palindrome)
                palindromes.append(int(palindrome))
        i += 1

    palindromes = [_ for _ in list(set(palindromes)) if a <= _ <= b]
    return palindromes

if __name__ == '__main__':
    import os

    samples = [
        (1, 4),
        (10, 120),
        (100, 1000)
    ]

    for sample in samples:
        print(count_fair_and_square_numbers(*sample))

    data_files = ['C-small-practice',]
                #   'C-large-practice-1',
                #   'C-large-practice-2']
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
