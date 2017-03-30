#!/usr/bin/env python

from __future__ import print_function
from collections import deque

def get_last_word(s):
    word_q = deque()
    for letter in s:
        if len(word_q) == 0:
            word_q.append(letter)
        elif letter >= word_q[0]:
            word_q.appendleft(letter)
        else:
            word_q.append(letter)
    return ''.join(word_q)

if __name__ == '__main__':
    samples = ['CAB',
               'JAM',
               'CODE',
               'ABAAB',
               'CABCBBABC',
               'ABCABCABC',
               'ZXCASDQWE']
    for sample in samples:
        print(get_last_word(sample))

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for in_ in inputs:
                output_file.write('Case #{0}: {1}\n'.format(i, get_last_word(in_)))
                i += 1
