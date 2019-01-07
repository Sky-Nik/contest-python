import sys
n, m = map(int, input().split())
sdc = [tuple(map(int, input().split())) for _ in range(m)]
isdc = list(enumerate(sdc))
isdc.sort(key=lambda _: _[1][1])
a = [0 for _ in range(n + 1)]
for i, sdc in isdc:
	s, d, c = sdc
	a[d] = m + 1
for i, sdc in isdc:
	s, d, c = sdc
	for k in range(s, d):
		if a[k] == 0 and c > 0:
			a[k] = i + 1 # zero-based index
			c -= 1
	if c > 0:
		print(-1)
		sys.exit(0)
print(*a[1:])
