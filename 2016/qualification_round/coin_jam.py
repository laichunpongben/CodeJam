#!/usr/bin/env python

from __future__ import print_function
import itertools

def get_coins(length):
    if length >= 2 and isinstance(length, int):
        permutations = list(itertools.product(['0', '1'], repeat=length-2))
        return ['1' + ''.join(list(t)) + '1' for t in permutations]
    else:
        raise ValueError

def is_coin_jam(coin):
    if len(coin) < 2:
        return False
    if not coin[0].startswith('1'):
        return False
    if not coin[-1].startswith('1'):
        return False

    for base in range(2, 11):
        base10_int = int(coin, base)
        if is_prime(base10_int):
            return False

    return True

def is_prime(n):
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
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def get_coin_jams(length, required_count):
    coins = get_coins(length)
    coin_jams = []
    for coin in coins:
        if is_coin_jam(coin):
            coin_jams.append(coin)
        if len(coin_jams) >= required_count:
            return coin_jams
    return None


if __name__ == '__main__':
    print(get_coin_jams(6, 3))

    with open('C-small-practice.in', 'r') as input_file:
        lines = input_file.readlines()
    input_count = int(lines[0].replace('\n' ,''))
    inputs = [tuple([int(_) for _ in line.replace('\n', '').split(' ')]) for line in lines[1:]]

    for in_ in inputs:
        n, j = in_
        print(get_coin_jams(n, j))

    # i = 1
    # with open('B-small-practice.out', 'w') as output_file:
    #     for in_ in inputs:
    #         output_file.write('Case #{0}: {1}\n'.format(i, get_last_num(in_)))
    #         i += 1
