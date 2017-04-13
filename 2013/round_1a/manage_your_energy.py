#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2013
# Round 1A 2013
# Problem B. Manage Your Energy

# Solved small test set

from __future__ import print_function
from operator import mul

def calc_max_gain(e, r, n, vs):
    assert isinstance(vs, list)

    spans = [0] * n
    for i in range(n):
        for j in range(i, n):
            if vs[j] > vs[i]:
                spans[i] = j - i
                break

    energies = [0] * n
    energy_start = e
    for i in range(n):
        if spans[i] > 0:
            energies[i] = max(min(energy_start, energy_start - e + spans[i] * r), 0)
        else:
            energies[i] = energy_start
        energy_start += -energies[i]
        assert energy_start >= 0
        energy_start += r

    print('n', n)
    print('spans', spans)
    print('energies', energies)

    return sum(map(mul, vs, energies))

if __name__ == '__main__':
    import os

    samples = [
        (5, 2, 2, [2, 1]),
        (5, 2, 2, [1, 2]),
        (3, 3, 4, [4, 1, 3, 5])
    ]

    for sample in samples:
        print(calc_max_gain(*sample))

    data_files = ['B-small-practice', 'B-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]
        erns = inputs[::2]
        vss = inputs[1::2]

        test_cases = []
        for i in range(input_count):
            ern = tuple([int(_) for _ in erns[i].split(' ')])
            vs = [int(_) for _ in vss[i].split(' ')]
            test_case = (ern[0], ern[1], ern[2], vs)
            test_cases.append(test_case)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                output_file.write('Case #{0}: {1}\n'.format(i, calc_max_gain(*test_case)))

                i += 1
