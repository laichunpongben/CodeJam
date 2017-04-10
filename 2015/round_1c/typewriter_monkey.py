
from __future__ import print_function, division
import itertools
import re

def get_overlapping_size(seq):
    overlapping_size = 0
    for i in range(1, len(seq)):
        if seq[-i:] == seq[:i]:
            overlapping_size = i
        else:
            break
    return overlapping_size

def calc_max_banana(k, l, s, keyboard, target):
    assert all(c in keyboard for c in target)

    if s >= l:
        overlapping_size = get_overlapping_size(target)
        return int((s - l) / (l - overlapping_size)) + 1
    else:
        return 0

def calc_expected_banana(k, l, s, keyboard, target):
    permutations = itertools.product(keyboard, repeat=s)
    return

def calc_expected_banana_kept(k, l, s, keyboard, target):
    max_banana = calc_max_banana(k, l, s, keyboard, target)
    expected_banana = calc_expected_banana(k, l, s, keyboard, target)
    return max_banana - expected_banana

if __name__ == '__main__':
    import os

    samples = [
        (7, 6, 6, 'BANANAS', 'MONKEY'),
        (2, 3, 4, 'AA', 'AAA'),
        (2, 1, 2, 'AB', 'B'),
        (6, 2, 2, 'GOOGLE', 'GO'),
        (26, 11, 100, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ROSENCRANTZ')
    ]
