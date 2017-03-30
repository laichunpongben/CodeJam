#!/usr/bin/env python
# Small: Wrong; Large: Need to solve time complexity

from __future__ import print_function
from collections import deque

def get_score(mood_lineup):
    score = 0
    grouping = split_symmetric_groups(mood_lineup)
    for g in grouping:
        if is_symmetric(g):
            score += len(g) * 5.0
        else:
            score += len(g) * 2.5
    return int(score)

def split_symmetric_groups(s):
    grouping = [s]
    while True:
        print('grouping', grouping)
        for g in grouping:
            for length in range(len(g), 0, -2):
                if all(is_symmetric(g) for g in grouping):
                    return grouping

                if all(len(g) == 2 for g in grouping):
                    return grouping

                if length == 2:
                    pairing = [item[0] + item[1] for item in zip(g[::2], g[1::2])]
                    print('pairing', pairing)
                    try:
                        grouping.remove(g)
                    except ValueError:
                        print('Remove error')
                        print(grouping)
                        print(g)
                        break
                    grouping.extend(pairing)
                    break

                for start in range(0, len(g)+length+2, 2):
                    g0 = g[:start]
                    g1 = g[start:start+length]
                    g2 = g[start+length:]
                    print('g0', g0, 'g1', g1, 'g2', g2)
                    if is_symmetric(g1):
                        try:
                            grouping.remove(g)
                        except ValueError:
                            print('Remove error')
                            print(grouping)
                            print(g)
                            break
                        grouping.extend([_ for _ in [g0, g1, g2] if len(_) > 0])

def is_symmetric(s):
    dq = deque(s)
    dq.reverse()
    s_ = ''.join(dq)
    return s == s_ and len(s) > 0

if __name__ == '__main__':
    import os

    samples = [
        'CCJJ',
        'CJCJ',
        'CJJC',
        'CJJJ',
        'CCCCCC'
    ]

    for sample in samples:
        print(get_score(sample))

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
                output_file.write('Case #{0}: {1}\n'.format(i, get_score(in_)))
                i += 1
