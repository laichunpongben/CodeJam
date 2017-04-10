from __future__ import print_function
import itertools
from functools import reduce
import operator

def build_sk_dict():
    sk_dict = {}
    # with open('skd_large.csv', 'w') as data:
    for s in range(2, 11):
        sk_dict[s] = {}
        for k in range(2, s+1):
            sk_dict[s][k] = []
            xors = [int('1' * k, 2) * (2 ** j) for j in range(s - k + 1)]
            for r in range(s - k + 2):
                combo = itertools.combinations(xors, r)
                for c in combo:
                    zxor = reduce(operator.xor, c, 0)
                    print(s, k, zxor, r, c)
                    # data.write('{0} {1} {2} {3}\n'.format(s, k, zxor, r))

if __name__ == '__main__':
    build_sk_dict()
