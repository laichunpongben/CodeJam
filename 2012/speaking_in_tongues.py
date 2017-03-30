#!/usr/bin/env python

from __future__ import print_function
import string

ENCRYPT_KEY = 'ynficwlbkuomxsevzpdrjgthaq'

def get_g2s_dict(encrypt_key):
    assert len(encrypt_key) == 26

    translation = zip(encrypt_key, string.lowercase)
    return {t[0]: t[1] for t in translation}

def decrypt(g):
    g2s_dict = get_g2s_dict(ENCRYPT_KEY)
    s = ''
    for c in g:
        if c == ' ':
            s += ' '
        else:
            s += g2s_dict[c]
    return s

if __name__ == '__main__':
    import os
    
    samples = [
        'ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    ]

    for sample in samples:
        print(decrypt(sample))

    data_files = ['A-small-practice']
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
                output_file.write('Case #{0}: {1}\n'.format(i, decrypt(in_)))
                i += 1
