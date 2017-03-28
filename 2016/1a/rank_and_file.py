#!/usr/bin/env python

from __future__ import print_function
import random

def get_missing_line(survey):
    if not isinstance(survey, list):
        raise TypeError
    if len(survey) % 2 == 0:
        raise ValueError

    n = (len(survey) + 1) / 2

    while True:
        rows = sorted(random.sample(survey, n))
        columns = sorted(survey[:])
        for row in rows:
            columns.remove(row)

        rows_as_columns = map(list, zip(*rows))

        try:
            for column in columns:
                rows_as_columns.remove(column)
        except ValueError:
            continue

        if len(rows_as_columns) == 1:
            return rows_as_columns[0]

if __name__ == '__main__':
    sample = [[1,2,3],
              [2,3,5],
              [3,5,6],
              [2,3,4],
              [1,2,3]]
    print(get_missing_line(sample))

    data_files = ['B-small-practice', 'B-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        test_case_count = int(lines[0].replace('\n' ,''))
        test_cases = []
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 0
        while i < len(inputs):
            n = int(inputs[i])
            survey = [[int(_) for _ in line.split(' ')] for line in inputs[i+1:i+2*n]]
            test_cases.append(survey)
            i += 2*n

        j = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for test_case in test_cases:
                result = ' '.join([str(_) for _ in get_missing_line(test_case)])
                output_file.write('Case #{0}: {1}\n'.format(j, result))
                j += 1
