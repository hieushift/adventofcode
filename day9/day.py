d = [int(x.replace('\n', '')) for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import sys
sys.setrecursionlimit(100000)

import re
p = re.compile("^(?P<outer>.*) bags contain (?P<list>.*).$")
innerP = re.compile("^(?P<number>\d*) (?P<type>.*) (bag|bags)$")

q = d[:25]

for x in d[25:]:
    # tried = set()
    good = False
    for i in q:
        if good: break
        for j in q:
            if good: break
            if i+j == x:
                good = True
    if good:
        q = q[1:] + [x]
    else:
        print('bad: cant make {} from {}'.format(x, q))

y = 133015568
def check(i, j):
    if sum(d[i:j]) == y:
        print(min(d[i:j]), max(d[i:j]), i,j, '{}'.format(d[i:j]) )

i = 0
j = 2
for i in range(len(d)):
    for j in range(2, len(d)):
        check(i, j)


