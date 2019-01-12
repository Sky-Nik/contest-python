def gcd(x, y):
	while y != 0:
		x, y = y, x % y

	return x


T = int(input())

for Ti in range(T):
	N, t, x, y, z = map(int, input().split())

	if t == 3:
		x, z = z, x

	m, n = 1, 2 * N + 1

	if t == 1 or t == 3:
		if x + 1 == y:
			if y - 1 == z:
				m = y - 1
			elif y + 1 == z:
				m = n - (y + 1)
		elif x - 1 == y:
			if y - 1 == z:
				m = n - (y - 1)
			elif y + 1 == z:
				m = y + 1
	elif t == 2 or t == 4:
		m = n - (y - 1) - (y + 1)

	g = gcd(m, n)

	print(m // g, n // g)
