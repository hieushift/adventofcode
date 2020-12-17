d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)



mask_p = re.compile('^mask = ([01X]{36})$')
write_p = re.compile('^mem\[(\d*)\] = (\d*)$')

def set_bit(value, bit):
    m = 1 << bit
    value = value & ~m
    return value | (m)

mask = None
mem = {}
for line in d:
    if 'mask' in line:
        match = mask_p.search(line)
        mask = match[1]
    else:
        match = write_p.search(line)
        addr = match[1]
        val = int(match[2])
        for i, v in enumerate(mask):
            if v == '1' or v == 'X':
                addr[i] = v
        for a in get_all_addresses(addr):
            mem[a] = val
        print('writing {}'.format(bin(val)))
        mem[addr] = val
print(mem)
print(sum(mem.values()))
