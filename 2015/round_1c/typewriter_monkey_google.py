# Find the maximum amount of overlap. We can just try
# every possible amount and check which ones work.
def max_overlap(t):
    for i in range(1, len(t)):
        if t[i:] == t[0:len(t)-i]:
            return len(t) - i
    return 0.0

# Returns the probability of the target word
# occurring at a fixed place.
def probability(target, keyboard):
    P = 1.0
    # Compute the product of the probabilities
    # for each letter of the word being correct.
    for i in range(len(target)):
        # The probability for a single letter being correct
        # is the fraction of keys which are that letter.
        C = keyboard.count(target[i])
        P = P * C / len(keyboard);
    return P

if __name__ == '__main__':
    import os

    data_files = ['B-small-practice',]
                #   'B-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        k_l_ss = [line.split(' ') for line in inputs[::3]]
        ks, ls, ss = zip(*k_l_ss)
        ks = [int(_) for _ in ks]
        ls = [int(_) for _ in ls]
        ss = [int(_) for _ in ss]
        keyboards = [line for line in inputs[1::3]]
        targets = [line for line in inputs[2::3]]
        test_cases = zip(ks, ls, ss, keyboards, targets)

        print(test_cases)

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                K, L, S, keyboard, target = test_case
                P = probability(target, keyboard)
                res = 0.0
                if P > 0:
                    O = max_overlap(target)
                    max_copies = 1.0 + (S-L) / (L-O)
                    min_copies = P * (S-L+1)
                    res = max_copies - min_copies
                output_file.write('Case #{0}: {1}\n'.format(i, res))
                i += 1
