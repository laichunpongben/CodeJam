
from __future__ import print_function

import math

def is_tidy(n):
    s = str(n)
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def get_last_tidy_number(n):
    assert isinstance(n, (int, long))

    if is_tidy(n):
        return n

    digits = list(str(n))
    max_digit = max([int(_) for _ in digits])

    if max_digit == 1:
        return int('9' * (len(str(n))-1))

    for i in range(len(digits)):
        digit = int(digits[i])
        min_tidy = int(''.join(digits[:i] + [str(digit)] * (len(digits) - i)))
        # print('min_tidy', min_tidy, len(str(min_tidy)))
        if min_tidy > n:
            result = int(''.join(digits[:i] + [str(digit-1)] + ['9'] * (len(digits) - i - 1)))
            # print('len', len(str(result)))
            return result
        else:
            continue

    raise ValueError

    return 0


if __name__ == '__main__':
    samples = [
        132,
        1000,
        7,
        111111111111111110,
        1000000000000000000000000,
        999999999999999998,
        465456494618904980,
        498089465064560150,
        999989777790000030,
        100000000000564656,
        128887498984665464,
        132132121321561101,
        999999999999999999,
        987654321012345679,
        123456789999999998
    ]

    for sample in samples:
        print(get_last_tidy_number(sample))

    data_files = ['B-large',]
                #   'B-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [int(line.replace('\n', '')) for line in lines[1:]]

        i = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for in_ in inputs:
                n = int(in_)
                output_file.write('Case #{0}: {1}\n'.format(i, get_last_tidy_number(n)))
                i += 1
