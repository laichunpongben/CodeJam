#!/usr/bin/env python

from __future__ import print_function
import itertools

def get_artwork(sequence, complexity):
    if not isinstance(complexity, int):
        raise ValueError
    if complexity < 1:
        raise ValueError

    s = sequence.replace('G', '').replace('L', '')
    if len(s) > 0:
        raise ValueError

    k = len(sequence)

    current_sequence = sequence
    next_sequence = ''

    if complexity == 1:
        return sequence

    for layer in range(complexity-1):
        for tile in current_sequence:
            if tile == 'G':
                next_sequence += 'G'*k
            else:
                next_sequence += sequence
        current_sequence = next_sequence
    return next_sequence

def get_all_artwork(k, c):
    permutations = list(itertools.product(['G', 'L'], repeat=k))
    sequences = [''.join(list(p)) for p in permutations]
    return [get_artwork(seq, c) for seq in sequences]



if __name__ == '__main__':
    samples =  [(2,3,2),
                (1,1,1),
                (2,1,1),
                (2,1,2),
                (3,2,3)]
    for sample in samples:
        k, c, s = sample
        print(get_all_artwork(k, c))
