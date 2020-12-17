d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)


from collections import defaultdict
print(d)
your = False
nearby = False
good = set()

p = re.compile('^.*: (\d+)-(\d+) or (\d+)-(\d+)')
has_letters = re.compile('^[\d,]+$')

error = 0

class field:
    def __init__(self, name, r1, r2):
        self.r1 = r1
        self.r2 = r2
        self.name = name

    def check(self, num):
        return (self.r1[0] <= num <= self.r1[1]) or (self.r2[0] <= num <= self.r2[1])

fields = []
fields.append(field('departure location', (33,679), (691,971)))
fields.append(field('departure station', (48,646), (671,966)))
fields.append(field('departure platform', (37,601), (619,950)))
fields.append(field('departure track', (41,863), (875,973)))
fields.append(field('departure date', (37,145), (168,965)))
fields.append(field('departure time', (26,246), (257,972)))
fields.append(field('arrival location', (30,542), (556,960)))
fields.append(field('arrival station', (30,75), (89,954)))
fields.append(field('arrival platform', (48,274), (299,958)))
fields.append(field('arrival track', (41,561), (567,957)))
fields.append(field('class', (40,237), (243,952)))
fields.append(field('duration', (33,317), (336,972)))
fields.append(field('price', (47,365), (381,957)))
fields.append(field('route', (29,415), (435,951)))
fields.append(field('row', (45,762), (784,972)))
fields.append(field('seat', (34,888), (914,968)))
fields.append(field('train', (50,502), (513,960)))
fields.append(field('type', (45,802), (825,961)))
fields.append(field('wagon', (44,458), (475,963)))
fields.append(field('zone', (28,721), (735,972)))
bad_index = set([25, 26, 34, 37, 46, 47, 48, 58, 59, 67, 74, 81, 85, 89, 94, 96, 98, 106, 111, 116, 121, 124, 131, 134, 141, 143, 147, 149, 153, 154, 157, 161, 164, 167, 169, 180, 181, 189, 192, 198, 203, 204, 207, 208, 214, 224, 226, 247, 250, 253, 254, 261, 264])

good = []

for i, x in enumerate(d):
    m = has_letters.search(x)
    if m is None:
        continue
    elif i in bad_index:
        continue
    good.append([int(n) for n in x.split(',')])

cols = []

for i in range(len(good[0])):
    cols.append([r[i] for r in good])

possible = {}

for i, c in enumerate(cols):
    p = True
    for f in fields:
        if all([f.check(v) for v in c]):
            if i in possible:
                possible[i].append(f.name)
            else:
                possible[i] = [f.name]

print(possible)

known = {}


# while True:
#     vals = possible.values()
#     for idx, v in enumerate(vals):
#         for f in known.keys():
#             if f in v:
#                 v.remove(f)
#         if len(v) == 1:
#             known[v[0]] = idx
#             print(known)
#             continue
#
#
# print(known)
#
#
