"""
d = []
def read():
    d = [x.replace('\n', '') for x in open('day.txt').readlines()]


def read_test():
    d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]
"""

d = [x.replace('\n', '') for x in open('day.txt').readlines()]
# d = [x.replace('\n', '') for x in open('day_test.txt').readlines()]

import re
import math
import functools
import sys
sys.setrecursionlimit(100000)

