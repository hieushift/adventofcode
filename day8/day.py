d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]


import sys
sys.setrecursionlimit(100000)

import re
p = re.compile("^(?P<outer>.*) bags contain (?P<list>.*).$")
innerP = re.compile("^(?P<number>\d*) (?P<type>.*) (bag|bags)$")


def check(d):
    next = 0
    acc = 0
    seen = set()
    while True:
        if next >= len(d):
            if next == len(d):
                print(acc)
                return True
            raise Exception('{} too large'.format(next))
        l = d[next]
        k = '{}. {}'.format(next, l)
        if k in seen:
            print(acc)
            print('seen before: {}'.format(k))
            return False
            # break
        seen.add(k)
        ins, v = l.split(' ')
        if ins == 'nop':
            next += 1
            continue
        elif ins == 'acc':
            acc += int(v)
        elif ins == 'jmp':
            next += int(v)
            continue
        next += 1


# for i, x in enumerate(d):
#     d_copy = [n for n in d]
#     ins, v = x.split(' ')
#     if ins == 'jmp':
#         d_copy[i] = 'nop ' + v
#         if check(d_copy):
#             print('change line {} from jmp {} to nop'.format(i, v))
#     elif ins == 'nop':
#         d_copy[i] = 'jmp ' + v
#         if check(d_copy):
#             print('change line {} from nop {} to jmp'.format(i, v))

print(check(d))
