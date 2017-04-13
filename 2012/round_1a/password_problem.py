
from __future__ import print_function
from operator import mul

def calc_min_expected_keystrokes(len_password, ps):
    len_typed = len(ps)
    len_remaining = len_password - len_typed
    all_typed_correct = prod(ps)
    # print(all_typed_correct)

    def calc_expected_keystrokes_backspace(len_password, ps, backspace_count):
        if backspace_count > 0:
            return prod(ps[:-i]) * (i*2 + len_remaining + 1) + \
                   (1 - prod(ps[:-i])) * (i*2 + len_remaining + len_password + 2)
        else:
            return all_typed_correct * (len_remaining + 1) + \
                   (1 - all_typed_correct) * (len_remaining + len_password + 2)

    def calc_expected_keystrokes_enter(len_password, ps):
        if len_remaining == 0:
            return all_typed_correct + (1 - all_typed_correct) * (len_password + 2)
        else:
            return len_password + 2

    min_expected_keystrokes = float('inf')
    for i in range(len_typed + 1):
        expected_keystrokes = calc_expected_keystrokes_backspace(len_password, ps, i)
        # print(expected_keystrokes)
        min_expected_keystrokes = min(min_expected_keystrokes, expected_keystrokes)

    expected_keystrokes = calc_expected_keystrokes_enter(len_password, ps)
    # print(expected_keystrokes)
    min_expected_keystrokes = min(min_expected_keystrokes, expected_keystrokes)

    return min_expected_keystrokes

def prod(mylist):
    return reduce(mul, mylist, 1)

if __name__ == '__main__':
    import os

    samples = [
        [5, 0.6, 0.6],
        [20, 1],
        [4, 1.0, 0.9, 0.1]
    ]

    for sample in samples:
        len_password, ps = sample[0], sample[1:]
        print('{0:0.6f}'.format(calc_min_expected_keystrokes(len_password, ps)))

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        test_cases = zip([line.replace('\n', '') for line in lines[1::2]],
                         [line.replace('\n', '') for line in lines[2::2]])

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                len_password = int(test_case[0].split(' ')[1])
                ps = [float(_) for _ in test_case[1].split(' ')]
                print(len_password, ps)
                output_file.write('Case #{0}: {1}\n'.format(i, calc_min_expected_keystrokes(len_password, ps)))
                i += 1
