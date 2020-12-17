d = [x.replace('\n', '') for x in open('day3.txt').readlines()]

import math

width = len(d[0])
right = 1
down = 2
steps = math.ceil(len(d) / down)

trees = 0
for s in range(steps):
	print('row {} col {}'.format(s*down, (s*right%width)))
	r = d[s*down]
	if r[(s*right)%width] == '#': trees += 1

print(trees)
