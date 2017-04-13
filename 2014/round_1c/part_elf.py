
from __future__ import print_function, division
import decimal
from decimal import Decimal
import sys

ctx = decimal.getcontext()
ctx.prec = 42

def build_generation_dict(n):
    generation_dict = {k: [] for k in range(n)}
    generation_dict[0] = [Decimal('0'), Decimal('1')]
    grandparents = []
    parents = []

    for k in range(1, n):
        print(k)
        parents = generation_dict[k-1][:]
        grandparents = list(set(grandparents).union(set(parents)))
        children = [ctx.divide(i, (2 ** k)) for i in range(2 ** k)]
        # for parent in parents:
        #     for grandparent in grandparents:
        #         child = ctx.divide((parent + grandparent), 2)
        #         children.append(child)
        generation_dict[k] = list(set(children).difference(set(grandparents)))
        # print(generation_dict[k])

    return generation_dict

def get_min_generation(v, generation_dict):
    for k in range(n):
        if v in generation_dict[k]:
            return k
    return sys.maxint

if __name__ == '__main__':
    import os

    samples = [
        1/2,
        3/4,
        1/4,
        2/23,
        123/31488
    ]

    n = 20
    generation_dict = build_generation_dict(n)

    for sample in samples:
        min_generation = get_min_generation(sample, generation_dict)
        if min_generation == sys.maxint:
            print('impossible')
        else:
            print(min_generation)

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for in_ in inputs:
                line = in_.split('/')
                p, q = line
                v = ctx.divide(Decimal(str(p)), Decimal(str(q)))
                min_generation = get_min_generation(v, generation_dict)
                if min_generation == sys.maxint:
                    output_file.write('Case #{0}: impossible\n'.format(i))
                else:
                    output_file.write('Case #{0}: {1}\n'.format(i, min_generation))

                i += 1
