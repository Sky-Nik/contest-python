n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
sw = False
if n < m:
	sw = True
	a, b = b, a
	n, m = m, n
sa, sb = sum(a), sum(b)
v, k, s = abs(sa - sb), 0, []
for i in range(n):
	for j in range(m):
		d = abs(sa - sb + 2 * b[j] - 2 * a[i])
		if d < v:
			v = d
			k = 1
			s = [(i + 1, j + 1)]
p = {}
for i in range(n):
	for j in range(i):
		p[2 * (a[i] + a[j])] = (i, j)
p = list(p.items())
p.sort()
def bin(x):
	l, r = 0, len(p) - 1
	while l + 1 < r:
		m = (l + r) // 2
		if p[m][0] >= x:
			r = m
		if p[m][0] <= x:
			l = m
	return l, r
if n > 1:
	for i in range(m):
		for j in range(i):
			x = sa - sb + 2 * (b[i] + b[j])
			l, r = bin(x)
			_i, _j = p[l][1]
			d = abs(x - 2 * (a[_i] + a[_j]))
			if d < v:
				v = d
				k = 2
				s = [(_i + 1, i + 1), (_j + 1, j + 1)]
			_i, _j = p[r][1]
			d = abs(sa - sb + 2 * (b[i] + b[j]) - 2 * (a[_i] + a[_j]))
			if d < v:
				v = d
				k = 2
				s = [(_i + 1, i + 1), (_j + 1, j + 1)]
print(v)
print(k)
if sw:
	for p in s:
		print(*p[::-1])
else:
	for p in s:
		print(*p)
