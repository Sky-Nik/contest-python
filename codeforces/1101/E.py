n = int(input())

X, Y = 0, 0

for i in range(n):
	t, x, y = input().split()

	x, y = int(x), int(y)

	x, y = min(x, y), max(x, y)

	if t == '+':
		X, Y = max(x, X), max(y, Y)

	if t == '?':
		print('YES' if X <= x and Y <= y else 'NO')
