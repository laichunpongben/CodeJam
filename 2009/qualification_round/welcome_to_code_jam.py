#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2009
# Qualification Round 2009
# Problem C. Welcome to Code Jam

from __future__ import print_function

SUBSTRING = 'welcome to code jam'

def count_welcome(s):
    if len(s) < len(SUBSTRING):
        return 0

    count = 1

    indexes = []
    last_index = 0
    for c in SUBSTRING:
        last_index = s.find(c, last_index)
        indexes.append(last_index)

    print(indexes)

def generate_index(s):
    for c in SUBSTRING:


if __name__ == '__main__':
    import os

    samples = [
        'elcomew elcome to code jam',
        'wweellccoommee to code qps jam',
        'welcome to codejam'
    ]

    for sample in samples:
        print(count_welcome(sample))
