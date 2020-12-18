d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)


d = [x.split(' ') for x in d]

left = []
depth = 0
ops = []
first_left = []

def flush():
    global first_left
    global ops
    global left
    f_left = 0
    if len(first_left) > 0:
        f_left = first_left.pop()
    left, left_now = left[:f_left], left[f_left:]
    ops, ops_now = ops[:-(len(left_now) - 1)], ops[-(len(left_now) - 1):]
    out = left_now[0]
    left_now = left_now[1:]

    todo = [out]
    for i, op in enumerate(ops_now):
        if op == '*':
            todo.append(left_now[i])
        elif op == '+':
            todo[-1] += left_now[i]
    prod = 1
    for t in todo:
        prod *= t
    left.append(prod)

sums = []
for eq in d:
    left = []
    depth = 0
    ops = []
    first_left = []
    for part in eq:
        if part.startswith('('):
            a = part
            while a.startswith('('):
                depth += 1
                a = a[1:]
                first_left.append(len(left))
            left.append(int(a))
        elif part == '*' or part == '+':
            ops.append(part)
        else:
            if part.endswith(')'):
                right = int(part.replace(')', ''))
                left.append(right)
                for i in range(part.count(')')):
                    depth -= 1
                    flush()
            else:
                left.append(int(part))

    flush()
    if len(left) != 1:
        print('wtf')
    print(left[0])
    sums.append(left[0])

print(sum(sums))


# while len(ops) > 0:
#     right = left.pop()
#     op = ops.pop()
#     if op == '*':
#         left[-1] *= right
#     elif op == '+':
#         left[-1] += right

