def gcd(x, y):
	return x if y == 0 else gcd(y, x % y)


A = int(input())

n, d = 0, A - 2

for base in range(2, A):
	a = A
	while a > 0:
		n += a % base
		a //= base

g = gcd(n, d)

n, d = n // g, d // g

print(f'{n}/{d}')
