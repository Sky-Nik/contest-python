n, m = map(int, input().split())

a = [(i + 1, True) for i in range(m)]

for _ in range(n):
	l, r = map(int, input().split())

	for i in range(l, r + 1):
		a[i - 1] = (i, False)

a = list(filter(lambda _: _[1], a))

print(len(a))

print(' '.join(map(lambda _: str(_[0]), a)))
