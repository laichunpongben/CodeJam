#!/usr/bin/env python

from __future__ import print_function
import math
import random

def get_lineup(players):
    n = int(round(math.log(sum(players)) / math.log(2)))
    if 2 ** n != sum(players):
        raise ValueError

    lineups = []
    baseline_lineup = 'R' * players[0] + \
                      'P' * players[1] + \
                      'S' * players[2]

    num_trial = 10000
    for _ in range(num_trial):
        lineup = list(baseline_lineup)
        random.shuffle(lineup)
        lineup = ''.join(lineup)

        tournament_winner = get_tournament_winner(lineup)
        if tournament_winner:
            lineups.append(lineup)

    if len(lineups) > 0:
        return sorted(list(set(lineups)))[0]
    else:
        return 'IMPOSSIBLE'

def get_tournament_winner(lineup):
    old_lineup = lineup
    new_lineup = ''
    while True:
        pairing = zip(old_lineup[::2], old_lineup[1::2])
        for pair in pairing:
            try:
                winner = get_winner(pair)
            except TieException:
                return None
            new_lineup += winner

        if len(new_lineup) == 1:
            return new_lineup

        old_lineup = new_lineup
        new_lineup = ''

def get_winner(pair):
    if pair[0] == pair[1]:
        raise TieException
    elif 'R' not in pair:
        return 'S'
    elif 'P' not in pair:
        return 'R'
    elif 'S' not in pair:
        return 'P'
    else:
        raise ValueError

class TieException(Exception):
    pass

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

    data_files = ['A-large-practice']
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
                players = [int(_) for _ in in_.split(' ')[1:]]
                output_file.write('Case #{0}: {1}\n'.format(i, get_lineup(players)))
                i += 1
