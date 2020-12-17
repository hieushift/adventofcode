d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]


import sys
sys.setrecursionlimit(100000)

import re
p = re.compile("^(?P<outer>.*) bags contain (?P<list>.*).$")
innerP = re.compile("^(?P<number>\d*) (?P<type>.*) (bag|bags)$")

sum = 0
sets = []
d.append('')
for x in d:
    if x == '':
        f = sets[0]
        for s in sets[1:]:
            f = f.intersection(s)
        sum += len(f)
        sets = []
        continue
    s = set()
    for c in x:
        s.add(c)
    sets.append(s)

print(sum)

