
from __future__ import print_function, division
import itertools
# import re
import regex as re

def get_overlapping_size(seq):
    overlapping_size = 0
    for i in range(1, len(seq)):
        if seq[-i:] == seq[:i]:
            overlapping_size = i
        else:
            break
    return overlapping_size

def calc_max_banana(k, l, s, keyboard, target):
    if not all(c in keyboard for c in target):
        return 0.0

    if s >= l:
        overlapping_size = get_overlapping_size(target)
        return int((s - l) / (l - overlapping_size)) + 1
    else:
        return 0.0

def calc_expected_banana(k, l, s, keyboard, target):
    if not all(c in keyboard for c in target):
        return 0.0

    count_target = 0
    count_permutations = 0
    permutations = itertools.product(keyboard, repeat=s)
    for permutation in permutations:
        # print(permutation)
        count_permutations += 1
        word = ''.join(list(permutation))
        matches = re.findall(target, word, overlapped=True)
        # results = [match.group(0) for match in matches]
        count_target += len(matches)
    return count_target / count_permutations

def calc_expected_banana_kept(k, l, s, keyboard, target):
    max_banana = calc_max_banana(k, l, s, keyboard, target)
    expected_banana = calc_expected_banana(k, l, s, keyboard, target)
    return max_banana - expected_banana

# Find the maximum amount of overlap. We can just try
# every possible amount and check which ones work.
def max_overlap(t):
  for i in range(1, len(t)):
    if t[i:] == t[0:len(t)-i]:
      return len(t) - i
  return 0




if __name__ == '__main__':
    import os

    samples = [
        (7, 6, 6, 'BANANAS', 'MONKEY'),
        (2, 3, 4, 'AA', 'AAA'),
        (2, 1, 2, 'AB', 'B'),
        (6, 2, 2, 'GOOGLE', 'GO'),
        # (26, 11, 100, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ROSENCRANTZ')
    ]

    for sample in samples:
        # max_banana = calc_max_banana(*sample)
        # expected_banana = calc_expected_banana(*sample)
        expected_banana_kept = calc_expected_banana_kept(*sample)
        # print(max_banana, expected_banana)
        print(expected_banana_kept)

    data_files = ['B-small-practice',]
                #   'B-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        k_l_ss = [line.split(' ') for line in inputs[::3]]
        ks, ls, ss = zip(*k_l_ss)
        ks = [int(_) for _ in ks]
        ls = [int(_) for _ in ls]
        ss = [int(_) for _ in ss]
        keyboards = [line for line in inputs[1::3]]
        targets = [line for line in inputs[2::3]]
        test_cases = zip(ks, ls, ss, keyboards, targets)

        print(test_cases)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                expected_banana_kept = calc_expected_banana_kept(*test_case)
                print(i, expected_banana_kept)
                output_file.write('Case #{0}: {1}\n'.format(i, expected_banana_kept))
                i += 1
