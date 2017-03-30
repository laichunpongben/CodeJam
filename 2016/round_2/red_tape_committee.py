#!/usr/bin/env python
# Small: Wrong; Large: Need to solve time complexity

from __future__ import print_function
import random
import itertools
import operator
from functools import reduce

def get_max_p_tie(k, candidates):
    max_p_tie = 0.0

    potential_committee = list(set(itertools.combinations(candidates, k)))
    print('potential_committee', potential_committee)
    for committee in potential_committee:
        print('committee', committee)
        group0s = list(set(itertools.combinations(committee, k/2)))
        for group0 in group0s:
            group1 = list(committee[:])
            for member in group0:
                group1.remove(member)
            group1 = tuple(group1)
            print('group0', group0, 'group1', group1)

            p_tie = prod(group0) * prod([1 - x for x in group1]) + \
                    prod(group1) * prod([1 - x for x in group0])
            max_p_tie = max(max_p_tie, p_tie)

    return max_p_tie

def prod(factors):
    return reduce(operator.mul, factors, 1)

if __name__ == '__main__':
    import os

    samples = [
        (2, [0.50, 0.50]),
        (2, [0.00, 0.00, 1.00, 1.00]),
        (2, [0.75, 1.00, 0.50])
    ]
    for sample in samples:
        k, candidates = sample
        print(get_max_p_tie(k, candidates))

    data_files = ['B-small-practice', 'B-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        test_case_count = int(lines[0].replace('\n' ,''))
        test_cases = []
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 0
        while i < len(inputs):
            k = int(inputs[i].split(' ')[-1])
            candidates = [float(_) for _ in inputs[i+1].split(' ')]
            test_cases.append((k, candidates))
            i += 2

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                print(i)
                output_file.write('Case #{0}: {1}\n'.format(i, get_max_p_tie(*test_case)))
                i += 1
