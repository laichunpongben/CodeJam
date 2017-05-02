#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Round 1C 2017
# Problem B. Parenting Partnering

# Solved small test set

from __future__ import print_function, division


def mark_timeline(activities_j, activities_c):
    timeline = {t: '' for t in range(1440)}
    for a in activities_j:
        for t in range(a[0], a[1]):
            timeline[t] = 'j'

    for a in activities_c:
        for t in range(a[0], a[1]):
            timeline[t] = 'c'

    return sorted(timeline.items(), key=lambda x: x[0])

def solve(aj, ac, activities):
    activities_j = sorted(activities[:aj])
    if len(activities_j) > 1:
        activities_j2 = []
        for i, item in enumerate(activities_j):
            if i == 0:
                backward = activities_j[0][0] - activities_j[-1][1]
                forward = activities_j[1][0] - activities_j[0][1]
            elif i == len(activities_j) - 1:
                backward = activities_j[-1][0] - activities_j[-2][1]
                forward = activities_j[0][0] - activities_j[-1][1]
            else:
                backward = activities_j[i][0] - activities_j[i-1][1]
                forward = activities_j[i+1][0] - activities_j[i][1]

            if backward < 0:
                backward += 1440
            if forward < 0:
                forward += 1440

            activities_j2.append((activities_j[i][0], activities_j[i][1], backward, forward))

        activities_j = sorted(activities_j2, key=lambda x: (x[3], x[2], x[0], x[1]))

    activities_c = sorted(activities[aj:])
    if len(activities_c) > 1:
        print(activities_c)
        activities_c2 = []
        for i, item in enumerate(activities_c):
            if i == 0:
                backward = activities_c[0][0] - activities_c[-1][1]
                forward = activities_c[1][0] - activities_c[0][1]
            elif i == len(activities_c) - 1:
                backward = activities_c[-1][0] - activities_c[-2][1]
                forward = activities_c[0][0] - activities_c[-1][1]
            else:
                backward = activities_c[i][0] - activities_c[i-1][1]
                forward = activities_c[i+1][0] - activities_c[i][1]

            if backward < 0:
                backward += 1440
            if forward < 0:
                forward += 1440

            activities_c2.append((activities_c[i][0], activities_c[i][1], backward, forward))

        activities_c = sorted(activities_c2, key=lambda x: (x[3], x[2], x[0], x[1]))
        print(activities_c)

    time_activities_j = sum(a[1] - a[0] for a in activities_j)
    time_activities_c = sum(a[1] - a[0] for a in activities_c)

    timeline = mark_timeline(activities_j, activities_c)

    activity = 0
    if activities_j:
        first_j_min = activities_j[activity][0]
        while time_activities_j < 720:
            if timeline[first_j_min][1] == 'j':
                first_j_min += 1
            elif timeline[first_j_min][1] == 'c':
                activity += 1
                if activity >= len(activities_j):
                    break
                first_j_min = activities_j[activity][0]
            else:
                timeline[first_j_min] = (first_j_min, 'j')
                time_activities_j += 1
                first_j_min += 1

            if first_j_min >= 1440:
                first_j_min = 0

    activity = 0
    if activities_c:
        first_c_min = activities_c[activity][0]
        while time_activities_c < 720:
            if timeline[first_c_min][1] == 'c':
                first_c_min += 1
            elif timeline[first_c_min][1] == 'j':
                activity += 1
                if activity >= len(activities_c):
                    break
                first_c_min = activities_c[activity][0]
            else:
                timeline[first_c_min] = (first_c_min, 'c')
                time_activities_c += 1
                first_c_min += 1

            if first_c_min >= 1440:
                first_c_min = 0

    if len(activities_j) > 1:
        activities_j = sorted(activities_j2, key=lambda x: (x[2], x[3], x[0], x[1]))
        print(activities_j)
    if len(activities_c) > 1:
        activities_c = sorted(activities_c2, key=lambda x: (x[2], x[3], x[0], x[1]))
        print(activities_c)


    if activities_j:
        activity = len(activities_j) - 1
        first_j_min = activities_j[activity][0]
        while time_activities_j < 720:
            if timeline[first_j_min][1] == 'j':
                first_j_min += -1
            elif timeline[first_j_min][1] == 'c':
                activity += -1
                if activity < 0:
                    break
                first_j_min = activities_j[activity][0]
            else:
                timeline[first_j_min] = (first_j_min, 'j')
                time_activities_j += 1
                first_j_min += -1

            if first_j_min < 0:
                first_j_min = 1439

    if activities_c:
        activity = len(activities_c) - 1
        first_c_min = activities_c[activity][0]
        while time_activities_c < 720:
            if timeline[first_c_min][1] == 'c':
                first_c_min += -1
            elif timeline[first_c_min][1] == 'j':
                activity += -1
                if activity < 0:
                    break
                first_c_min = activities_c[activity][0]
            else:
                timeline[first_c_min] = (first_c_min, 'c')
                time_activities_c += 1
                first_c_min += -1

            if first_c_min < 0:
                first_c_min = 1439

    timeline = [x[1] for x in timeline]
    print(timeline)
    print(timeline.count('j'), timeline.count('c'))

    if timeline.count('j') >= 720:
        timeline = ['c' if x=='' else x for x in timeline]

    if timeline.count('c') >= 720:
        timeline = ['j' if x=='' else x for x in timeline]

    assert timeline.count('j') == 720
    assert timeline.count('c') == 720

    timeline = ''.join(timeline)

    exchange = 0
    exchange += timeline.count('jc')
    exchange += timeline.count('cj')
    if timeline[0] != timeline[-1]:
        exchange += 1

    return exchange

if __name__ == '__main__':
    import os

    samples = [
        (1, 1, [(540, 600), (840, 900)]),
        (2, 0, [(900, 1260), (180, 540)]),
        (1, 1, [(1439, 1440), (0, 1)]),
        (2, 2, [(0, 1), (1439, 1440), (1438, 1439), (1, 2)]),
        (3, 4, [(0, 10), (1420, 1440), (90, 100), (550, 600), (900, 950), (100, 150), (1050, 1400)])
    ]

    for sample in samples:
        print(solve(*sample))

    data_files = ['B-large']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        test_cases = []
        j = 0
        for _ in range(input_count):
            activities = []
            aj, ac = tuple([int(_) for _ in inputs[j].split(' ')])
            j += 1

            for _ in range(aj+ac):
                row = tuple([int(_) for _ in inputs[j].split(' ')])
                activities.append(row)
                j += 1
            test_cases.append((aj, ac, activities))

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                min_exchange = solve(*test_case)
                output_file.write('Case #{0}: {1}\n'.format(i, min_exchange))
                i += 1
