#!/usr/bin/env python

from __future__ import print_function
from functools import reduce

def split_candies(candies):
    assert isinstance(candies, list)

    partitions = sorted_k_partitions(candies, 2)
    print(partitions)

    max_candy = 0
    for partition in partitions:
        xor0 = reduce(lambda x, y: x ^ y, partition[0])
        sum0 = sum(partition[0])
        xor1 = reduce(lambda x, y: x ^ y, partition[1])
        sum1 = sum(partition[1])
        print(xor0, xor1, sum0, sum1)
        if xor0 == xor1:
            max_candy = max(max_candy, max(sum0, sum1))

    return max_candy

def sorted_k_partitions(seq, k):
    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    for item in generate_partitions(i + 1):
                        yield item  # Python3: yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                for item in generate_partitions(i + 1):
                    yield item  # Python3: yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    # Sort the parts in each partition in shortlex order
    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
    result = sorted(result, key = lambda ps: (len(ps), ps))  # Python3: *map(len, ps)

    return result

if __name__ == '__main__':
    import os

    samples = [
        [1,2,3,4,5],
        [3,5,6]
    ]

    for sample in samples:
        max_candy = split_candies(sample)
        if max_candy > 0:
            print(max_candy)
        else:
            print('NO')

    data_files = ['C-small-practice',
                  'C-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]
        test_cases = [[int(_) for _ in in_.split(' ')] for in_ in inputs[1::2]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                print(test_case)
                max_candy = split_candies(test_case)
                if max_candy > 0:
                    output_file.write('Case #{0}: {1}\n'.format(i, max_candy))
                else:
                    output_file.write('Case #{0}: {1}\n'.format(i, 'NO'))
                i += 1
