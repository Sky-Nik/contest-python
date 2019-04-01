#!/usr/bin/env python

n, a = int(input()), sorted(list(map(int, input().split())))

not_ok = any(a[i + 2] == a[i + 1] == a[i] for i in range(n - 2))

if not_ok:
	print('NO')
else:
	print('YES')

	x, y = [a[0]], []
	for i in range(n - 1):
		(y if a[i + 1] == a[i] else x).append(a[i + 1])

	print(len(x))
	print(*x)
	print(len(y))
	print(*y[::-1])
