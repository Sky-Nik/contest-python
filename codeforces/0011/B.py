def h(n):
	return (n + 1) * n // 2


x = abs(int(input()))

n, s = 0, 0

while (x > s) or (x % 2 != s % 2):
	n += 1
	s = h(n)

print(n)
