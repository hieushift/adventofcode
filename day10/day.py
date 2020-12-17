d = [int(x.replace('\n', '')) for x in open('day.txt').readlines()]
# d = [int(x.replace('\n', '')) for x in open('day_test.txt').readlines()]

import sys
sys.setrecursionlimit(100000)

d.sort()



import re
import math
# p = re.compile("^(?P<outer>.*) bags contain (?P<list>.*).$")
# innerP = re.compile("^(?P<number>\d*) (?P<type>.*) (bag|bags)$")

print(d)

one = 1
three = 1
phone = max(d) + 3

all = 0

m = {}
m[max(d)] = 1
def check(rest, curr, m):
    if curr in m:
        return m[curr]
    total = 0
    for x in rest:
        if x > curr + 3:
            break
        total += check(rest[1:], x, m)
    m[curr] = total
    return total


check(d, 0,m)
print(m[0])
