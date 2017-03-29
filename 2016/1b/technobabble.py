#!/usr/bin/env python

from __future__ import print_function
from collections import deque

def parse_and_sort_topics(topics):
    topic_deque = deque(tuple(topic.split(' ')) for topic in topics)
    word0s = [item[0] for item in topic_deque]
    word1s = [item[1] for item in topic_deque]
    topic_deque = deque(sorted(list(topic_deque),
                        key=lambda x: (word0s.count(x[0]) + word1s.count(x[1]),
                                       word1s.count(x[1]),
                                       word0s.count(x[0]))))

    sorted_topics = []
    while len(topic_deque) > 0:
        topic = topic_deque.popleft()
        sorted_topics.append(topic)

        added_word0s = [item[0] for item in sorted_topics]
        added_word1s = [item[1] for item in sorted_topics]

        topic_deque = deque(sorted(list(topic_deque),
                            key=lambda x: (added_word0s.count(x[0]) + added_word1s.count(x[1]),
                                           added_word1s.count(x[1]),
                                           added_word0s.count(x[0]),
                                           word0s.count(x[0]) + word1s.count(x[1]),
                                           word1s.count(x[1]),
                                           word0s.count(x[0]))))

    return sorted_topics

def count_fake(topics):
    word0_dict = {}
    word1_dict = {}
    real_count = 0
    fake_count = 0

    sorted_topics = parse_and_sort_topics(topics)
    print(sorted_topics)

    for topic in sorted_topics:
        word0, word1 = topic

        try:
            word0_count = word0_dict[word0]
        except KeyError:
            word0_dict[word0] = 0

        try:
            word1_count = word1_dict[word1]
        except KeyError:
            word1_dict[word1] = 0

        if word0_dict[word0] > 0 and word1_dict[word1] > 0:
            fake_count += 1
        else:
            real_count += 1

        word0_dict[word0] += 1
        word1_dict[word1] += 1

    return fake_count

if __name__ == '__main__':
    import os

    samples = [
        ['HYDROCARBON COMBUSTION',
         'QUAIL BEHAVIOR',
         'QUAIL COMBUSTION'],
        ['CODE JAM',
         'SPACE JAM',
         'PEARL JAM'],
        ['INTERGALACTIC PLANETARY',
         'PLANETARY INTERGALACTIC'],
        ['BOUNDARY GRAVITY',
         'BOUNDARY HERMENEUTICS',
         'BOUNDARY TRANSGRESSION',
         'QUANTUM GRAVITY',
         'QUANTUM HERMENEUTICS',
         'QUANTUM TRANSGRESSION',
         'TRANSFORMATIVE GRAVITY',
         'TRANSFORMATIVE HERMENEUTICS',
         'TRANSFORMATIVE TRANSGRESSION'],
        ['GF CH',
         'RO GI',
         'YB GI',
         'TD HI',
         'YG HI',
         'IZ NB',
         'BQ TA',
         'GF TP',
         'GR WG',
         'IZ ZD']
    ]
    for sample in samples:
        print(count_fake(sample))

    data_files = ['C-small-practice']
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
            topics = inputs[i+1:i+n+1]
            test_cases.append(topics)
            i += n+1

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for test_case in test_cases:
                print(i)
                output_file.write('Case #{0}: {1}\n'.format(i, count_fake(test_case)))
                i += 1
