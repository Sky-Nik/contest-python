#!/usr/bin/env python

n, a = int(input()), list(map(lambda _: int(_) - 1, input().split()))

c, d = 0, 0

while c < n:
	m = a[c]

	while m > c:
		c += 1
		m = max(m, a[c])

	c += 1
	d += 1

print(d)
