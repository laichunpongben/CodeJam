#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2016
# Qualification Round 2016
# Problem C. Coin Jam

# Solved all test sets

from __future__ import print_function

def get_coin(length, i):
    return '1' + format(i, '#0{0}b'.format(length))[2:] + '1'

def is_coin_jam(coin):
    if len(coin) < 2:
        return False
    if not coin[0].startswith('1'):
        return False
    if not coin[-1].startswith('1'):
        return False

    for base in range(2, 11):
        base10_int = int(coin, base)
        threshold = 1000
        if has_no_divisor_below(base10_int, threshold):
            return False

    return True

def has_no_divisor_below(n, threshold):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if i > threshold:
            break

        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def get_divisor(n):
    """Returns the divisor"""
    if n == 2:
        return None
    if n == 3:
        return None
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return None

def get_coin_jams(length, required_count):
    coin_jams = []
    i = 0
    while True:
        coin = get_coin(length, i)
        if is_coin_jam(coin):
            coin_and_disvisors = [coin]
            for base in range(2,11):
                base10_int = int(coin, base)
                divisor = get_divisor(base10_int)
                coin_and_disvisors.append(divisor)
            coin_jams.append(coin_and_disvisors)
        if len(coin_jams) >= required_count:
            return coin_jams
        i += 1
    return None

if __name__ == '__main__':
    print(get_coin_jams(6, 3))

    data_files = ['C-small-practice', 'C-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [tuple([int(_) for _ in line.replace('\n', '').split(' ')]) for line in lines[1:]]

        i = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for in_ in inputs:
                n, j = in_
                coin_jams = get_coin_jams(n, j)

                output_file.write('Case #{0}:\n'.format(i))
                for coin_jam in coin_jams:
                    output_file.write(' '.join([str(_) for _ in coin_jam]))
                    output_file.write('\n')

                i += 1
