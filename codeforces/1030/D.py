import sys


def gcd(x, y):
	while y != 0:
		x, y = y, x % y
	return x


n, m, k = map(int, input().split())

if 2 * n * m % k != 0:
	print('NO')
else:
	even = k % 2 == 0

	if even:
		k //= 2

	a, b = n, m
	
	g1 = gcd(a, k)

	a //= g1
	k //= g1

	g2 = gcd(b, k)

	b //= g2
	k //= g2

	if not even:
		if 2 * a <= n:
			a *= 2
		elif 2 * b <= m:
			b *= 2
		else:
			print('NO')
			sys.exit(0)

	print('YES')
	print(0, 0)
	print(a, 0)
	print(0, b)
