def gcd(x, y):
	while y != 0:
		x, y = y, x % y
	return x


n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

d, zeros = {0:0}, 0

for i in range(n):
	if a[i] == 0:
		if b[i] == 0:
			zeros += 1
		continue

	gi = gcd(a[i], b[i])
	a[i] //= gi
	b[i] //= gi

	if a[i] < 0:
		a[i] *= -1
		b[i] *= -1

	if (a[i], b[i]) not in d:
		d[(a[i], b[i])] = 0
	d[(a[i], b[i])] += 1

print(max(d.values()) + zeros)