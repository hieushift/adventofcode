d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

# d = ['@' * (len(d[0])+2)] + ['@' + x + '@' for x in d] + ['@' * (len(d[0])+2)]
d = [[c for c in s] for s in d]



import re
import math
import functools
import sys
sys.setrecursionlimit(100000)

# m = {1: 0}
# @functools.lru_cache(maxsize=128)
# def factorial(x):
#     if x == 0: return 1
#     return x * factorial(x - 1)

class Node:
    def __init__(self, r, c, val):
        self.row = r
        self.col = c
        self.val = val
        self.next_val = None
        self.neighbors = []

    def find_neighbors(self, g):
        for delta_r in [-1, 0, 1]:
            for delta_c in [-1, 0, 1]:
                if delta_r == 0 and delta_c == 0:
                    continue
                seat = self.find_seat(delta_r, delta_c, g)
                if seat is not None:
                    self.neighbors.append(seat)

    def find_seat(self, delta_r, delta_c, g):
        r = self.row
        c = self.col
        r += delta_r
        c += delta_c
        while r >= 0 and r < len(g) and c >= 0 and c <= len(g[0])-1:
            if g[r][c].val == 'L' or g[r][c].val == '#':
                return r, c
            r += delta_r
            c += delta_c
        return None

    def count_occupied_neighbors(self, g):
        sum = 0
        for r, c in self.neighbors:
            n = g[r][c]
            if n.val == '#': sum += 1
        return sum

    def set_next_val(self):
        if self.val == 'L' or self.val == '#':
            if self.next_val is not None:
                self.val = self.next_val
                self.next_val = None


seen = set()
g = [[m for m in x] for x in d]
for i in range(len(d)):
    for j in range(len(d[0])):
        g[i][j] = Node(i, j, g[i][j])

for i in range(len(g)):
    for j in range(len(g[0])):
        n = g[i][j]
        n.find_neighbors(g)

print(g)
seen = set()
cou = 0
while True:
    if cou == 1:
        print()
    for i in range(len(g)):
        for j in range(len(g[0])):
            n = g[i][j]
            if n.val == '#':
                if n.count_occupied_neighbors(g) >= 5:
                    n.next_val = 'L'
                else:
                    n.next_val = '#'
            elif n.val == 'L':
                if n.count_occupied_neighbors(g) == 0:
                    n.next_val = '#'
                else:
                    n.next_val = 'L'
            g[i][j] = n


    for i in range(len(g)):
        for j in range(len(g[0])):
            n = g[i][j]
            n.set_next_val()

    h = ''.join([''.join([x.val for x in y]) for y in g])
    if h in seen:
        print(h.count('#'))
        break
    seen.add(h)
    cou += 1
