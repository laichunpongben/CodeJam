from __future__ import print_function



def get_style_point_and_models(n, m, preplaced_models=[]):

    preplaced_model_dict = {k: [] for k in ('+', 'x', 'o')}
    for preplaced_model in preplaced_models:
        model_type = preplaced_model[0]
        position = preplaced_model[1]
        preplaced_model_dict[model_type].append(position)

    # print(preplaced_model_dict)

    style_point = 0
    models = []

    if preplaced_model_dict['o']:
        o_row = preplaced_model_dict['o'][0][0]
        o_col = preplaced_model_dict['o'][0][1]
    elif preplaced_model_dict['x']:
        o_row = preplaced_model_dict['x'][0][0]
        o_col = preplaced_model_dict['x'][0][1]
    else:
        o_row = 1
        o_col = 1

    if n == 1:
        style_point = 2
        models.append(('o', (1,1)))
        for preplaced_model in preplaced_models:
            if preplaced_model in models:
                models.remove(preplaced_model)
        return style_point, models

    models.append(('o', (o_row, o_col)))
    x_row, x_col = o_row, o_col
    for i in range(n-1):
        if o_col <= x_col < n:
            x_row += 1
            x_col += 1
        elif x_col == n:
            x_row = n
            x_col = 1
        else:
            x_row += -1
            x_col += 1
        models.append(('x', (x_row, x_col)))

    p_row = 1
    p_col = 0
    for i in range(n):
        p_col += 1
        if p_col == o_col:
            continue
        else:
            models.append(('+', (p_row, p_col)))

    p_row = n
    p_col = 0
    for i in range(n):
        p_col += 1
        if p_col == 1:
            continue
        elif p_col == n:
            continue
        else:
            models.append(('+', (p_row, p_col)))

    style_point = 3 * n - 2

    for preplaced_model in preplaced_models:
        if preplaced_model in models:
            models.remove(preplaced_model)

    return style_point, models


if __name__ == '__main__':
    samples = [
        # (2, 0, []),
        # (2, 1, [('x', (1,2))]),
        # (1, 1, [('o', (1,1))]),
        # (3, 1, [('o', (1,1))]),
        # (3, 4, [('+', (2,3)),
        #         ('+', (2,1)),
        #         ('x', (3,1)),
        #         ('+', (2,2)),
        #        ]),
    ]

    for sample in samples:
        style_point, models = get_style_point_and_models(*sample)
        print(style_point)
        print(models)
        print()

    data_files = ['D-small-attempt0',]
                #   'D-large-practice']
    for f in data_files:
        with open('{0}.in'.format(f), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        test_cases = []
        i = 0
        for j in range(input_count):
            n, m = tuple([int(_) for _ in inputs[i].split(' ')])
            pms = []
            if m > 0:
                for k in range(m):
                    i += 1
                    line = tuple([_ for _ in inputs[i].split(' ')])
                    model_type = line[0]
                    row = int(line[1])
                    col = int(line[2])
                    pms.append((model_type, (row, col)))

            test_cases.append((n, m, pms))
            i += 1

        z = 1
        with open('{0}.out'.format(f), 'w') as output_file:
            for test_case in test_cases:
                style_point, models = get_style_point_and_models(*test_case)
                output_file.write('Case #{0}: {1} {2}\n'.format(z, style_point, len(models)))
                for model in models:
                    model_type = model[0]
                    row = model[1][0]
                    col = model[1][1]
                    output_file.write('{0} {1} {2}\n'.format(model_type, row, col))
                z += 1
