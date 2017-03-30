#!/usr/bin/env python

from __future__ import print_function

def parse_senates(senates_str):
    return [int(_) for _ in senates_str.split(' ')]

def get_evacuation_plan(senates):
    if not isinstance(senates, list):
        raise TypeError

    num_parties = len(senates)
    remaining_senates = senates[:]
    evacuation = []

    while sum(remaining_senates) > 0:
        sorted_index = get_sorted_index(remaining_senates)
        party_index0, party_index1 = sorted_index[:2]
        if remaining_senates[party_index0] > 0:
            evacuated_party0 = get_party(party_index0)
            evacuation.append(evacuated_party0)

        if remaining_senates[party_index1] > 0:
            evacuated_party1 = get_party(party_index1)
            evacuation.append(evacuated_party1)

        evacuation.append(' ')

        remaining_senates[party_index0] += -1
        remaining_senates[party_index1] += -1

    evacuation_plan = ''.join(evacuation)[:-1]
    if evacuation_plan[-2] == ' ':
        evacuation_plan = evacuation_plan[:-3] + ' ' + evacuation_plan[-3] + evacuation_plan[-1]

    return evacuation_plan

def get_sorted_index(seq):
    return sorted(range(len(seq)), key=lambda i:-seq[i])

def get_party(party_index):
    return chr(party_index + 65)

if __name__ == '__main__':
    import os

    samples = ['2 2',
               '3 2 2',
               '1 1 2',
               '2 3 1']

    for sample in samples:
        senates = parse_senates(sample)
        print(get_evacuation_plan(senates))

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[2::2]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for in_ in inputs:
                senates = parse_senates(in_)
                output_file.write('Case #{0}: {1}\n'.format(i, get_evacuation_plan(senates)))
                i += 1
