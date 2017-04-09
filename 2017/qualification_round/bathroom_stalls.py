
from __future__ import print_function
import math

def get_min_max_ls_rs(n, k):
    rank = int(math.log(k, 2))
    position = k - 2 ** rank
    # print('rank', rank, 'position', position)

    remaining_stalls = max(n - 2 ** (rank + 1) + 1, 0)
    # print('remaining_stalls', remaining_stalls)

    residual_stall = remaining_stalls % (2 ** (rank+1))
    # print('residual_stall', residual_stall)

    stall = float(remaining_stalls) / (2 ** (rank+1))
    # print('stall', stall)

    high = int(stall)
    low = int(stall)
    # print('highlow', high, low)
    if position < residual_stall:
        high += 1

    residual_stall += - 2 ** (rank)

    if position < residual_stall:
        low += 1

    return high, low

if __name__ == '__main__':
    samples = [
        (2, 1),
        (2, 2),
        (3, 1),
        (3, 2),
        (3, 3),
        (4, 1),
        (4, 2),
        (5, 1),
        (5, 2),
        (6, 1),
        (6, 2),
        (7, 1),
        (7, 2),
        (7, 3),
        (7, 4),
        (8, 1),
        (8, 2),
        (8, 3),
        (8, 4),
        (8, 5),
        (1000, 1000),
        (1000, 1),
        (999, 1),
        (1000, 2),
        (999, 2),
        (1000, 3),
        (1000, 4),
        (1000, 5),
        (1000, 6),
        (1000, 7),
        (1000, 8),
        (660, 100),
        (1000000000000000000, 1)

    ]

    for sample in samples:
        print(sample)
        print(get_min_max_ls_rs(*sample))
        print()

    data_files = ['C-large',]
                #   'C-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for in_ in inputs:
                line = tuple([int(_) for _ in in_.split(' ')])
                n, k = line
                high, low = get_min_max_ls_rs(n, k)
                output_file.write('Case #{0}: {1} {2}\n'.format(i, high, low))
                i += 1
