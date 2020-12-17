d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)


forward = 'E'
dir_to_val = {'E': 1, 'W': -1, 'N': 1, 'S': -1}

turn_right = {
    'E': ['S', 'W', 'N'],
    'S': ['W', 'N', 'E'],
    'W': ['N', 'E', 'S'],
    'N': ['E', 'S', 'W'],
}
turn_left = {
    'E': ['N', 'W', 'S'],
    'S': ['E', 'N', 'W'],
    'W': ['S', 'E', 'N'],
    'N': ['W', 'S', 'E'],
}

east = 0
north = 0

east_w = 10
north_w = 1

for ins in d:
    letter = ins[0]
    val = int(ins[1:])
    if letter == 'F':
        east += val * east_w
        north += val * north_w
    elif letter == 'L':
        if val == 90:
            north_w, east_w  = east_w, -north_w
        elif val == 180:
            north_w, east_w  = -north_w, -east_w
        elif val == 270:
            north_w, east_w  = -east_w, north_w
    elif letter == 'R':
        if val == 90:
            north_w, east_w  = -east_w, north_w
        elif val == 180:
            north_w, east_w  = -north_w, -east_w
        elif val == 270:
            north_w, east_w  = east_w, -north_w
    elif letter == 'N':
        north_w += val
    elif letter == 'S':
        north_w -= val
    elif letter == 'E':
        east_w += val
    elif letter == 'W':
        east_w -= val
    else:
        raise 'wtf'

print(east, north)

print(abs(east) + abs(north))
