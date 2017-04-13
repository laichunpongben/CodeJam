

from __future__ import print_function

class Osmos(object):
    def __init__(self, my_mote, n, motes):
        self.my_mote = my_mote
        self.n = n
        self.motes = motes
        self.operations = 0
        self.can_absorb = True

    def absorb(self):
        min_mote = min(self.motes)
        if min_mote < self.my_mote:
            self.my_mote += min_mote
            self.motes.remove(min_mote)
            if self.motes:
                return True
            else:
                return False
        return False

    def create(self):
        self.motes.append(self.my_mote - 1)
        self.operations += 1

    def remove(self):
        self.motes.remove(max(self.motes))
        self.operations += 1

    def play(self):
        while self.motes:
            while self.can_absorb:
                self.can_absorb = self.absorb()

            if self.motes:
                if self.my_mote * 2 - 1 > min(self.motes):
                    self.create()
                else:
                    self.remove()

            self.can_absorb = True

        return self.operations

if __name__ == '__main__':
    import os

    samples = [
        (2, 2, [2, 1]),
        (2, 4, [2, 1, 1, 6]),
        (10, 4, [25, 20, 9, 100]),
        (1, 4, [1, 1, 1, 1])
    ]

    for sample in samples:
        osmos = Osmos(*sample)
        print(osmos.play())

    data_files = ['A-small-practice', 'A-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]
        ans = inputs[::2]
        motess = inputs[1::2]

        test_cases = []
        for i in range(input_count):
            an = tuple([int(_) for _ in ans[i].split(' ')])
            motes = [int(_) for _ in motess[i].split(' ')]
            test_case = (an[0], an[1], motes)
            test_cases.append(test_case)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                osmos = Osmos(*test_case)
                output_file.write('Case #{0}: {1}\n'.format(i, osmos.play()))

                i += 1
