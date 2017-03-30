#!/usr/bin/env python

from __future__ import print_function
import math
from copy import deepcopy

def get_lineup(players):
    if not isinstance(players, tuple):
        raise TypeError

    n = int(round(math.log(sum(players)) / math.log(2)))
    if 2 ** n != sum(players):
        raise ValueError

    lineup_dict = build_lineup_dict(n)
    lineups = sorted([lineup_dict[n][winner] for winner in ('R', 'P', 'S')])
    
    for lineup in lineups:
        count = count_players(lineup)
        if players == count:
            return lineup

    return 'IMPOSSIBLE'

def build_lineup_dict(n):
    lineup_dict = dict.fromkeys(range(n+1), {})

    for winner in ('R', 'P', 'S'):
        lineup_dict[0][winner] = winner

    for i in range(1, n+1):
        r = deepcopy(lineup_dict[i-1]['R'])
        p = deepcopy(lineup_dict[i-1]['P'])
        s = deepcopy(lineup_dict[i-1]['S'])

        lineup_dict[i]['R'] = min(r, s) + max(r, s)
        lineup_dict[i]['P'] = min(p, r) + max(p, r)
        lineup_dict[i]['S'] = min(p, s) + max(p , s)

    return lineup_dict

def count_players(lineup):
    r = lineup.count('R')
    p = lineup.count('P')
    s = lineup.count('S')
    return r, p, s

if __name__ == '__main__':
    import os

    samples = [
        (1,1,0),
        (2,0,0),
        (1,1,2),
        (2,0,2)
    ]

    for sample in samples:
        print(get_lineup(sample))

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
                players = tuple([int(_) for _ in in_.split(' ')[1:]])
                output_file.write('Case #{0}: {1}\n'.format(i, get_lineup(players)))
                i += 1
