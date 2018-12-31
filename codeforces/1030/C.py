n = int(input())

a = list(map(int, list(input())))

OK = False

if a == [0 for _ in range(n)]:
	OK = True
	
else:
	s = sum(a)

	for i in range(1, s):
		if s % i == 0:
			c, j = 0, 0
			while c < i and j < n:
				c += a[j]
				if c == i:
					c = 0
				j += 1
			if c > i:
				continue
			if j == n:
				OK = True

print('YES' if OK else 'NO')
