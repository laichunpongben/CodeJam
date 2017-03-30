#!/usr/bin/env python

from __future__ import print_function
from collections import deque
import random

def get_rows_columns_greedy(survey):
    if not isinstance(survey, list):
        raise TypeError
    if len(survey) % 2 == 0:
        raise ValueError

    n = (len(survey) + 1) / 2
    s = deque(sorted(survey[:]))

    rows = []
    columns = []
    no_pair_line = None

    i = 0
    while i < n:
        print(i)
        print(s)
        if len(s) > 1:
            if s[0][i] == s[1][i]:
                line0 = s.popleft()
                line1 = s.popleft()
                if (not rows) and (not columns):
                    rows.append(line0)
                    columns.append(line1)
                else:
                    print('line0', line0)
                    print('line1', line1)
                    print('first_row', rows[0])
                    print('first_col', columns[0])

                    if line0[0] == rows[0][-1] and line1[0] == columns[0][-1] and line[0] != line1[0]:
                        print('38')
                        is_row_then_column = False
                    elif line0[0] == columns[0][-1] and line1[0] == rows[0][-1] and line[0] != line1[0]:
                        print('41')
                        is_row_then_column = True
                    else:
                        comparison_line0_rows = zip(rows[-1], line0)
                        comparison_line1_columns = zip(columns[-1], line1)
                        comparison_line0_columns = zip(columns[-1], line0)
                        comparison_line1_rows = zip(rows[-1], line1)

                        if all([item[0] < item[1] for item in comparison_line0_rows]) and \
                           all([item[0] < item[1] for item in comparison_line1_columns]) and \
                           not(all([item[0] < item[1] for item in comparison_line0_columns]) and \
                              all([item[0] < item[1] for item in comparison_line1_rows])):
                            print('48')
                            is_row_then_column = True
                        elif all([item[0] < item[1] for item in comparison_line0_columns]) and \
                               all([item[0] < item[1] for item in comparison_line1_rows]) and \
                               not(all([item[0] < item[1] for item in comparison_line0_rows]) and \
                                  all([item[0] < item[1] for item in comparison_line1_columns])):
                                print('55')
                                is_row_then_column = False
                        else:
                            print('62')
                            p = random.uniform(0, 1)
                            if p < 0.5:
                                is_row_then_column = True
                            else:
                                is_row_then_column = False

                    if is_row_then_column:
                        rows.append(line0)
                        columns.append(line1)
                    else:
                        rows.append(line1)
                        columns.append(line0)
            else:
                no_pair_line = s.popleft()
        else:
            no_pair_line = s.popleft()

        i += 1

    return rows, columns, no_pair_line

def get_missing_line(survey):
    if not isinstance(survey, list):
        raise TypeError
    if len(survey) % 2 == 0:
        raise ValueError

    n = (len(survey) + 1) / 2

    while True:
        rows, columns, no_pair_line = get_rows_columns_greedy(survey)
        print('rows', rows)
        print('columns', columns)
        print('no_pair_line', no_pair_line)

        rows_copy = rows[:]
        columns_copy = columns[:]

        rows_copy.append(no_pair_line)
        rows_copy.sort()
        transpose = map(list, zip(*rows_copy))
        print('transpose', transpose)

        try:
            for column in columns_copy:
                print('column', column)
                transpose.remove(column)
            break
        except ValueError:
            rows_copy = rows[:]
            columns_copy = columns[:]

            columns_copy.append(no_pair_line)
            columns_copy.sort()
            transpose = map(list, zip(*columns_copy))
            print('transpose', transpose)

            try:
                for row in rows_copy:
                    print('row', row)
                    transpose.remove(row)
                break
            except ValueError:
                print('126')
                continue

    if len(transpose) == 1:
        return transpose[0]
    else:
        raise ValueError

if __name__ == '__main__':
    import os
    import time

    sample = [[1,2,3],
              [2,3,5],
              [3,5,6],
              [2,3,4],
              [1,2,3]]
    print(get_missing_line(sample))

    start_time = time.time()

    data_files = ['B-small-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                '{0}.in'.format(f)), 'r') as input_file:
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
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                print(j)
                missing_line = get_missing_line(test_case)
                print('missing_line', missing_line)
                result = ' '.join([str(_) for _ in missing_line])
                output_file.write('Case #{0}: {1}\n'.format(j, result))
                j += 1

    end_time = time.time()
    lapsed_secs = end_time - start_time
    print(lapsed_secs)
