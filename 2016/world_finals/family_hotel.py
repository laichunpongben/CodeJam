#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2016
# World Finals 2016
# Problem B. Family Hotel




























def calc_p_occupied(n, k):
    p_occupied = 0
    for item in distribution:
        end_rooms, p_end_rooms = item
        if not k in end_rooms:
            p_occupied += p_end_rooms
    return p_occupied







def get_end_rooms(n):
    return []

if __name__ == '__main__':
    samples = [
        (3, 1),
        (3, 2),
        (4, 1),
        (4, 2)
    ]



















aa
