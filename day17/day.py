d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

dirs = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            for l in range(-1, 2):
                if i == 0 and j == 0 and k == 0 and l == 0:
                    continue
                dirs.append((i, j, k, l))
print(len(dirs))

def to_id(c):
    return '{},{},{},{}'.format(c[0], c[1], c[2], c[3])

print(dirs)
nodes = {}
class Node():
    def __init__(self, x, y, z, w, active):
        self.coords = (x, y, z, w)
        self.active = active
        self.next_active = self.active
        self.neighbors = []
        for d in dirs:
            n_coords = (
                x + d[0],
                y + d[1],
                z + d[2],
                w + d[3],
            )
            self.neighbors.append(n_coords)

    def update_state(self):
        self.active = self.next_active

edge = len(d[0])
x = 0
least = -6
max_xy = 14
max_wz = 7
for i in range(least, max_xy):
    for j in range(least, max_xy):
        for w in range(least, max_wz):
            for k in range(least, max_wz):
                x += 1
                n = Node(i, j, k, w, False)
                id = to_id((i, j, k, w))
                if 0 <= i < edge and 0 <= j < edge and k == 0 and w == 0:
                    n.active = d[i][j] == '#'
                nodes[id] = n
print(len(nodes.keys()))
print(x)

def print_d():
    for w in range(least, max_wz):
        for z in range(least, max_wz):
            x = 0
            coords = []
            for i in range(least, max_xy):
                for j in range(least, max_xy):
                    id = to_id((i, j, z, w))
                    n = nodes[id]
                    if n.active:
                        x+= 1
                        coords.append((i, j))
            print('w={}, z={}, {} active at {}'.format(w, z, x, coords))

cycle = 1
# print_d()
while cycle <= 6:
    print('cycle {}'.format(cycle))
    for id, node in nodes.items():
        active_count = 0
        if id == '0,2,-1,-1':
            print()
        for nb_dirs in node.neighbors:
            nb_id = to_id(nb_dirs)
            nb = nodes.get(nb_id, None)
            if nb is None:
                continue
            if nb.active:
                active_count += 1
        if node.active:
            if 2 <= active_count <= 3:
                node.next_active = True
            else:
                node.next_active = False
        else:
            if active_count == 3:
                node.next_active = True
            else:
                node.next_active = False

    for node in nodes.values():
        node.update_state()
    # print_d()

    cycle += 1

sum = 0
for n in nodes.values():
    if n.active: sum += 1
print(sum)
