d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)

# num -> turn #
spoken = {}
last_number = -1

d = [int(x) for x in d[0].split(',')]

said = [x for x in d]

turn = 0
for i, x in enumerate(d):
    turn += 1
    if x in spoken:
        first_time = False
    spoken[x] = turn
    last_number = x

said.append(0)

stop = 30000000
for i in range(len(d), stop):
    last_number = said[-1]
    if last_number in spoken:
        next = len(said) - spoken[last_number]
        spoken[last_number] = len(said)
        last_number = next
    elif last_number not in spoken:
        spoken[last_number] = len(said)
        last_number = 0
    first_time = last_number not in spoken
    turn += 1
    said.append(last_number)

print(len(said))
print(said[-2])
print(last_number)
