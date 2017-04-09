
from __future__ import print_function
import random
import sys
import itertools
import operator
import math

def flip(s, k, positions):
    # print(type(positions))
    assert isinstance(positions, tuple)
    s0 = s
    for position in positions:
        s_flip = s0[position:position + k]
        s0_flip = ''
        for c in s_flip:
            if c == '+':
                s0_flip += '-'
            else:
                s0_flip += '+'
        # print(s0[:position], s0_flip, s0[position + k:])
        s0 = s0[:position] + s0_flip + s0[position + k:]
    return s0

def flip_all_patterns(s, k):
    pattern_distance_dict = {}
    if k > len(s):
        pattern_distance_dict['+'*len(s)] = (0, len(s), 0, int(math.ceil(float(len(s))/2)), 0, int(float(len(s))/2), 0)
        return pattern_distance_dict

    if '-' not in s:
        pattern_distance_dict[s] = (0, len(s), 0, int(math.ceil(float(len(s))/2)), 0, int(float(len(s))/2), 0)

    r = range(len(s) - k + 1)
    for t in range(1, len(r) + 1):
        permutations = itertools.product(r, repeat=t)
        for permutation in permutations:
            # print(permutation)
            s0 = flip(s, k, permutation)
            # print(s0, len(permutation))
            step = len(permutation)
            count_p = s0.count('+')
            count_m = s0.count('-')

            s1 = s0[::2]
            # print('s1', s1)
            count_p_s1 = s1.count('+')
            count_m_s1 = s1.count('-')

            s2 = s0[1::2]
            # print('s2', s2)
            count_p_s2 = s2.count('+')
            count_m_s2 = s2.count('-')

            try:
                if step < pattern_distance_dict[s0][0]:
                    pattern_distance_dict[s0] = (step, count_p, count_m, count_p_s1, count_m_s1, count_p_s2, count_m_s2)
            except KeyError:
                pattern_distance_dict[s0] = (step, count_p, count_m, count_p_s1, count_m_s1, count_p_s2, count_m_s2)
    return pattern_distance_dict

# def get_flip_step(s, k):
#     s0 = s
#     count = 0
#     while '-' in s0:
#         s0 = flip(s0, k)
#         # print(s0)
#         count += 1
#
#         if count >= 100000:
#             return sys.maxint
#
#     return count
#
#
# def get_min_flip_step(s, k):
#     min_flip_step = sys.maxint
#     for i in range(1000):
#         step = get_flip_step(s, k)
#         min_flip_step = min(step, min_flip_step)
#     return min_flip_step

if __name__ == '__main__':
    samples = [
        # ('++', 2),
        # ('+++', 2),
        # ('++++', 2),
        # ('+++++', 2),
        # ('++++++', 2),
        # ('+++++++', 2),
        # ('+'*10, 5),
        # ('++++', 3),
        # ('+++++', 3),
        # ('+++++', 4),
        # ('+'*100, 3)
        # ('---+-++-', 3),
        # ('+++++', 4),
        # ('-+-+-', 4),
        # ('---+-++++', 3),
        # ('---+-++++', 2),
        # ('---+-++++', 4),
    ]

    samples = [('+' * len_s, k) for k in range(2, 11) for len_s in range(1, 11)]

    with open('skd.txt', 'w') as data:
        for sample in samples:
            s, k = sample
            print('s', s, 'len_s', len(s), 'k', k)
            # print('*' * 10)
            # print(get_min_flip_step(*sample))
            d = flip_all_patterns(*sample)
            # print(d)
            sorted_d = sorted(d.items(), key=operator.itemgetter(1))
            for item in sorted_d:
                print(item[0], item[1])
                data.write('{0} {1} {2}\n'.format(k, item[0], item[1][0]))
            print()
