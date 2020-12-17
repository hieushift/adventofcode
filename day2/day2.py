d = [x.replace('\n', '') for x in open('day2.txt').readlines()]
import re
p = re.compile('(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]+): (?P<password>.*)')
test = [p.search(x) for x in d]
all = [{'min': int(x.group('min')), 'max': int(x.group('max')), 'letter': x.group('letter'), 'password': x.group('password')} for x in test]

count = 0
for x in all:
	a = x['min'] - 1
	b = x['max'] - 1
	if b < len(x['password']) and ((x['password'][a] == x['letter']) ^ (x['password'][b] == x['letter'])): count += 1
print(count)
