d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

buses = [int(x) if x.isnumeric() else None for x in d[1].split(',')]

n = []
a = []
for i, x in enumerate(buses):
    if x is None: continue
    n.append(x)
    a.append(-i)


print(chinese_remainder(n, a))

836524002700652
100000000000000


def get_x(a_i, m):
    b_i = m/v


