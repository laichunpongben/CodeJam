#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2010
# Qualification Round 2010
# Problem C. Theme Park

# Solved all test sets

from __future__ import print_function, division
from collections import deque

def get_cycle(r, k, n, gs):
    assert isinstance(gs, list)

    gq = deque(gs)
    index = 0
    indexes = [0]

    rides = []

    if sum(gs) <= k:
        return 1, 0

    while True:
        roller_coaster = []
        remaining_seat = k
        while remaining_seat > 0 and gq:
            if gq[0] <= remaining_seat:
                g = gq.popleft()
                roller_coaster.append(g)
                remaining_seat += -g
                index += 1
                if index == n:
                    index = 0
            else:
                break
        rides.append(k - remaining_seat)
        indexes.append(index)
        gq.extend(roller_coaster)
        if len(indexes) != len(set(indexes)):
            cycle_start = indexes[-1]
            index_cycle_start = indexes.index(indexes[-1])
            cycle = len(indexes) - index_cycle_start - 1
            return cycle, cycle_start, index_cycle_start, rides

def get_rides(r, k, n, gs):
    assert isinstance(gs, list)

    if sum(gs) <= k:
        return r * sum(gs)
    else:
        cycle, cycle_start, index_cycle_start, rides = get_cycle(r, k, n, gs)
        rides_before_cycle = sum(rides[:index_cycle_start])
        rides_per_cycle = sum(rides[index_cycle_start:])

        if r >= cycle + index_cycle_start:
            sum_rides = rides_before_cycle
            r += -index_cycle_start

            sum_rides += int(r / cycle) * rides_per_cycle
            r = r % cycle

            rides_cycle = rides[index_cycle_start:]
            sum_rides += sum(rides_cycle[:r])
            return sum_rides
        else:
            return sum(rides[:r])

if __name__ == '__main__':
    import os

    samples = [
        (4, 6, 4, [1, 4, 2, 1]),
        (100, 10, 1, [1]),
        (5, 5, 10, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3])
    ]

    for sample in samples:
        print(get_rides(*sample))

    data_files = ['C-small-practice', 'C-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]
        rkns = inputs[::2]
        gss = inputs[1::2]

        test_cases = []
        for i in range(input_count):
            rkn = tuple([int(_) for _ in rkns[i].split(' ')])
            gs = [int(_) for _ in gss[i].split(' ')]
            test_case = (rkn[0], rkn[1], rkn[2], gs)
            test_cases.append(test_case)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                output_file.write('Case #{0}: {1}\n'.format(i, get_rides(*test_case)))

                i += 1
