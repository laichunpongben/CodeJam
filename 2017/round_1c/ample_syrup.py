#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Round 1C 2017
# Problem A. Ample Syrup

# Solved small test set

from __future__ import print_function, division
import math
import itertools


def get_k_highest_pancakes(n_pancakes, k):
    n_pancakes = sorted(n_pancakes, key=lambda x: -x[1])
    return n_pancakes[:k]

def get_k_largest_pancakes(n_pancakes, k):
    n_pancakes = sorted(n_pancakes, key=lambda x: -x[0])
    return n_pancakes[:k]

def get_k_pancakes(n_pancakes, k):
    n_pancakes = sorted(n_pancakes, key=lambda x: -(x[0] ** 2 + 2 * x[0] * x[1]))
    return n_pancakes[:k]

def get_exposed_area(pancakes):
    pancakes = sorted(pancakes, key=lambda x: -x[0])
    largest_r_pancake = pancakes[0]
    horizontal = math.pi * largest_r_pancake[0] ** 2
    vertical_total = 0
    for pancake in pancakes:
        r, h = pancake
        vertical = h * 2 * math.pi * r
        vertical_total += vertical
    return vertical_total + horizontal

def solve(n, k, pancakes):
    pancakes_high = get_k_highest_pancakes(pancakes, k)
    area_high = get_exposed_area(pancakes_high)

    pancakes_large = get_k_largest_pancakes(pancakes, k)
    area_large = get_exposed_area(pancakes_large)

    return max(area_large, area_high)

    max_area = 0
    potential_combo = itertools.combinations(pancakes, k)
    for c in potential_combo:
        area = get_exposed_area(c)
        if area > max_area:
            print(pancakes)
            print(n, k)
            print(c)
            print()
            max_area = area

    return max_area

if __name__ == '__main__':
    import os

    samples = [
        (2, 1, [(100, 20), (200, 10)]),
        (2, 2, [(100, 20), (200, 10)]),
        (3, 2, [(100, 10), (100, 10), (100, 10)]),
        (4, 2, [(9, 3), (7, 1), (10, 1), (8, 4)]),
    ]

    for sample in samples:
        print(solve(*sample))

    data_files = ['A-large']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        test_cases = []
        j = 0
        for _ in range(input_count):
            pancakes = []
            n, k = tuple([int(_) for _ in inputs[j].split(' ')])
            j += 1

            for _ in range(n):
                row = tuple([int(_) for _ in inputs[j].split(' ')])
                pancakes.append(row)
                j += 1
            test_cases.append((n, k, pancakes))

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                area = solve(*test_case)
                output_file.write('Case #{0}: {1:0.6f}\n'.format(i, area))
                i += 1
