d = [x for x in open('day4.txt').readlines()]
#d = [x for x in open('day4_test.txt').readlines()]
print(d)

passports = []
c = {}
for x in d:
	if x == '\n':
		passports.append(c)
		c = {}
		continue
	a = x.replace('\n', '').split(' ')
	for i in a:
		s = i.split(':')
		k = s[0]
		v = s[1]
		c[k] = v
passports.append(c)

expect = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
expect.sort()

import re 
eye = re.compile('^#[0-9a-f]{6}$')
pidp = re.compile('^[0-9]{9}$')
hclgood = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
good = 0
for p in passports:
	print(p)
	k = list(p.keys())
	if 'cid' in k: k.remove('cid')
	k.sort()
	print(k)
	if k != expect:
		print('bad: keys')
		continue
	try:
		byr = p['byr']
		if int(byr) < 1920 or int(byr) > 2002:
			print('bad byr {}'.format(byr))
			continue
		if int(p['iyr']) < 2010 or int(p['iyr']) > 2020:
			print('bad iyr {}'.format(iyr))
			continue
		if int(p['eyr']) < 2020 or int(p['eyr']) > 2030:
			continue
		hgt = p['hgt']
		h = int(p['hgt'][:-2])
		if hgt.endswith('cm'):
			if h < 150 or h > 193: continue
		elif hgt.endswith('in'):
			if h < 59 or h > 76: continue
		else:
			continue	
		if eye.match(p['hcl']) is None: continue
		if pidp.match(p['pid']) is None: continue
		if p['ecl'] not in hclgood: continue
		good += 1
	except:
		continue
	

print(good)
