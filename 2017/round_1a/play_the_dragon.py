#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Round 1A 2017
# Problem C. Play the Dragon

from __future__ import print_function, division
import math
import sys
import random


class Game(object):
    def __init__(self, hd, ad, hk, ak, b, d):
        self.hd = hd
        self.ad = ad
        self.hk = hk
        self.ak = ak
        self.b = b
        self.d = d

        self.dragon = Dragon(hd, ad, b, d)
        self.knight = Knight(hk, ak)
        self.turn = 0
        self.actions = []

    def buff(self):
        self.dragon.ad += self.dragon.b
        self.actions.append('B')
        self.turn += 1

    def debuff(self):
        self.knight.ak += -self.dragon.d
        self.knight.ak = max(self.knight.ak, 0)
        self.actions.append('D')
        self.turn += 1

    def cure(self):
        self.dragon.hd = self.dragon.max_hd
        self.actions.append('C')
        self.turn += 1

    def d_attack(self):
        self.knight.hk += -self.dragon.ad
        self.actions.append('A')
        self.turn += 1

    def k_attack(self):
        self.dragon.hd += -self.knight.ak

    def is_dragon_alive(self):
        return self.dragon.hd > 0

    def is_knight_alive(self):
        return self.knight.hk > 0

    def reset(self):
        self.dragon = Dragon(self.hd, self.ad, self.b, self.d)
        self.knight = Knight(self.hk, self.ak)
        self.turn = 0
        self.actions = []

    def calc_optimal_buff(self):
        if self.dragon.b == 0:
            return 0

        min_buff_plus_attack_turn = sys.maxint
        optimal_buff_turn = sys.maxint
        buff_turn = 0

        while True:
            buff_plus_attack = self.dragon.ad + buff_turn * self.dragon.b
            buff_plus_attack_turn = math.ceil(self.knight.hk / buff_plus_attack) + buff_turn
            # print(buff_plus_attack_turn)

            if buff_plus_attack_turn <= min_buff_plus_attack_turn:
                min_buff_plus_attack_turn = buff_plus_attack_turn
                optimal_buff_turn = buff_turn
                if min_buff_plus_attack_turn <= 1:
                    break
                buff_turn += 1
            else:
                break

        return optimal_buff_turn

    def calc_debuff_thesholds(self):
        if self.dragon.d == 0:
            return [0]

        turn_to_kill_dragon = math.ceil(self.dragon.max_hd / self.knight.ak)
        debuff_thesholds = [0]

        while True:
            knight_debuffed_attack = int(math.ceil(self.dragon.max_hd / turn_to_kill_dragon - 1))
            debuff_theshold = int(math.ceil(max(self.knight.ak - knight_debuffed_attack, 0) / self.dragon.d))
            debuff_thesholds.append(debuff_theshold)
            if knight_debuffed_attack <= 0:
                break
            turn_to_kill_dragon += 1

        return sorted(list(set(debuff_thesholds)))
        # return list(range(100))

    def play(self):
        min_turn = sys.maxint
        max_turn = 10000
        actions = []
        last_action = ''
        optimal_buff = self.calc_optimal_buff()
        print('b', optimal_buff)
        debuff_thesholds = self.calc_debuff_thesholds()
        print('d', debuff_thesholds)

        for debuff_theshold in debuff_thesholds:
            for _ in range(max_turn):
                if self.is_dragon_alive() and self.is_knight_alive():
                    turn_to_kill_knight_now = math.ceil(self.knight.hk / self.dragon.ad)
                    turn_to_kill_knight_buff = math.ceil(self.knight.hk / (self.dragon.ad + self.dragon.b)) + 1

                    try:
                        turn_to_kill_dragon_now = math.ceil(self.dragon.hd / self.knight.ak)
                    except ZeroDivisionError:
                        turn_to_kill_dragon_now = sys.maxint

                    try:
                        turn_to_kill_dragon_debuff = math.ceil(self.dragon.hd / max(self.knight.ak - self.dragon.d, 0))
                    except ZeroDivisionError:
                        turn_to_kill_dragon_debuff = sys.maxint

                    # print('turn', self.turn, 'A')
                    # print(self.dragon.ad, self.knight.hk, math.ceil(self.dragon.ad / self.knight.hk))
                    # print('turn_to_kill_knight_now', turn_to_kill_knight_now)
                    # print('turn_to_kill_dragon_now', turn_to_kill_dragon_now)
                    # print('turn_to_kill_knight_buff', turn_to_kill_knight_buff)
                    # print('turn_to_kill_dragon_debuff', turn_to_kill_dragon_debuff)

                    if turn_to_kill_knight_now <= 1:
                        # print('ATTACK')
                        self.d_attack()
                    elif turn_to_kill_dragon_debuff > 1 and turn_to_kill_dragon_now == 1:
                        # print('DEBUFF')
                        self.debuff()
                    elif turn_to_kill_dragon_now == 1:
                        # print('CURE')
                        self.cure()
                    elif self.actions.count('D') < debuff_theshold:
                        # print('DEBUFF')
                        self.debuff()
                    elif self.actions.count('B') < optimal_buff:
                        # print('BUFF')
                        self.buff()
                    else:
                        # print('ATTACK')
                        self.d_attack()

                    if last_action == 'C' and self.actions[-1] == 'C':
                        self.turn = sys.maxint
                        break

                    last_action = self.actions[-1]

                else:
                    break

                if self.is_knight_alive():
                    self.k_attack()
                else:
                    break

                # print('turn', self.turn, 'B')
                # print('dragon', self.dragon.hd, self.dragon.ad, self.knight.hk, self.knight.ak)
                # print()

                if not self.is_dragon_alive():
                    self.turn = sys.maxint
                    break

            print(debuff_theshold, self.turn)

            if self.turn <= min_turn:
                min_turn = self.turn
                actions = self.actions

            self.reset()


        print(actions)

        return min_turn


class Dragon(object):
    def __init__(self, hd, ad, b, d):
        self.max_hd = hd
        self.hd = hd
        self.ad = ad
        self.b = b
        self.d = d


class Knight(object):
    def __init__(self, hk, ak):
        self.hk = hk
        self.ak = ak

if __name__ == '__main__':
    import os

    samples = [
        (11, 5, 16, 5, 0, 0),
        (3, 1, 3, 2, 2, 0),
        (3, 1, 3, 2, 1, 0),
        (2, 1, 5, 1, 1, 1)
    ]

    # for sample in samples:
    #     min_turn = sys.maxint
    #     for _ in range(1):
    #         game = Game(*sample)
    #         turn = game.play()
    #         min_turn = min(turn, min_turn)
    #     if min_turn == sys.maxint:
    #         print('IMPOSSIBLE')
    #     else:
    #         print(min_turn)

    data_files = ['C-small-practice',]
    #  'B-large-practice']
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
                print('Case #{0}'.format(i))
                test_case = tuple([int(_) for _ in in_.split(' ')])
                print(test_case)
                min_turn = sys.maxint
                for _ in range(1):
                    game = Game(*test_case)
                    turn = game.play()
                    min_turn = min(turn, min_turn)
                if min_turn == sys.maxint:
                    output_file.write('Case #{0}: IMPOSSIBLE\n'.format(i))
                    print('IMPOSSIBLE')
                else:
                    output_file.write('Case #{0}: {1}\n'.format(i, min_turn))
                    print(min_turn)
                print()

                i += 1
