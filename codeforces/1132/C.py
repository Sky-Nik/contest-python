n, q = map(int, input().split())

lri = []

for i in range(q):
	l, r = map(int, input().split())
	lri.append((l, 'l', i))
	lri.append((r + 1, 'r', i))  # converts [l_i, r_i] to [l_i, r_i)

lri.sort()

total, cs, cc, cp, ci, msc = 0, set(), 0, 0, 0, dict()

while cp <= n:
	cp += 1
	
	while ci < 2 * q and lri[ci][0] == cp:
		if lri[ci][1] == 'l':
			cs.add(lri[ci][2])
			cc += 1
		
		if lri[ci][1] == 'r':
			cs.remove(lri[ci][2])
			cc -= 1
		
		ci += 1

	if cc > 0:
		total += 1

	if cc == 1:
		for c in cs:
			if c not in msc:
				msc[c] = 0
			msc[c] += 1

	if cc == 2:
		tc = tuple(sorted(tuple(cs)))
		if tc not in msc:
			msc[tc] = 0
		msc[tc] += 1

ans = 0

for i in range(q):
	cur = total
	if i in msc:
		cur -= msc[i]
	for j in range(i + 1, q):
		if j in msc:
			cur -= msc[j]
		if (i, j) in msc:
			cur -= msc[(i, j)]
		ans = max(ans, cur)

print(ans)
