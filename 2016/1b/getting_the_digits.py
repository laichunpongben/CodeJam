#!/usr/bin/env python

from __future__ import print_function
import string

DIGIT_DICT = {
    'ZERO': (0, 1),
    'ONE': (1, 0),
    'TWO': (2, 0),
    'THREE': (3, 0),
    'FOUR': (4, 0),
    'FIVE': (5, 0),
    'SIX': (6, 2),
    'SEVEN': (7, 0),
    'EIGHT': (8, 0),
    'NINE': (9, 0)
}

def get_letter_count_dict(s):
    return {c: s.count(c) for c in string.uppercase}

def get_digit_count_dict(s):
    letter_count_dict = get_letter_count_dict(s)
    digit_count_dict = dict.fromkeys(range(10), 0)

    for key in sorted(DIGIT_DICT.keys(),
                      key=lambda x: (-DIGIT_DICT[x][1], -len(x), x)):
        while all(letter_count_dict[letter] > 0 for letter in key):
            digit = DIGIT_DICT[key][0]
            digit_count_dict[digit] += 1
            for letter in key:
                letter_count_dict[letter] += -1

    if sum(letter_count_dict.values()) > 0:
        raise ValueError

    return digit_count_dict

def get_digits(s):
    digits = ''
    digit_count_dict = get_digit_count_dict(s)
    for digit in sorted(digit_count_dict.keys()):
        digits += str(digit) * digit_count_dict[digit]
    return digits

if __name__ == '__main__':
    import os

    samples = ['OZONETOWER',
               'WEIGHFOXTOURIST',
               'OURNEONFOE',
               'ETHER',
               'OEIHGERTZ',
               'EIVEOUXISEFNRFSV',
               'NESINOEOX']

    for s in samples:
        print(get_digits(s))

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
                output_file.write('Case #{0}: {1}\n'.format(i, get_digits(in_)))
                i += 1
