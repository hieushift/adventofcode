d = [x.replace('\n', '') for x in open('day.txt').readlines()]
d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

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
            if i == 0 and j == 0 and k == 0:
                continue
            dirs.append((i, j, k))

def to_id(c):
    return '{}{}{}'.format(c[0], c[1], c[2])

print(dirs)
nodes = {}
class Node():
    def __init__(self, x, y, z, active):
        self.coords = (x, y, z)
        self.active = active
        self.next_active = self.active
        self.neighbors = []
        for d in dirs:
            n_coords = (
                x + d[0],
                y + d[1],
                z + d[2],
            )
            self.neighbors.append(n_coords)

    def update_state(self):
        self.active = self.next_active

edge = len(d[0])
for i in range(-8, 15):
    for j in range(-8, 15):
        for k in range(-6, 7):
            n = Node(i, j, k, False)
            if 0 <= i < edge and 0 <= j < edge and k == 0:
                n = Node(i, j, k, d[i][j] == '#')
            nodes[to_id((i, j, k))] = n
print(len(nodes.keys()))

def print_d():
    for z in range(-6, 7):
        x = 0
        coords = []
        for i in range(-8, 15):
            for j in range(-8, 15):
                id = to_id((i, j, z))
                n = nodes[id]
                if n.active:
                    x+= 1
                    coords.append((i, j))
        print('z={}, {} active at {}'.format(z, x, coords))

cycle = 1
print_d()
while cycle <= 6:
    print('cycle {}'.format(cycle))
    for id, node in nodes.items():
        active_count = 0
        if id == '00-1' or id == '010':
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
    print_d()

    cycle += 1

sum = 0
for n in nodes.values():
    if n.active: sum += 1
print(sum)
