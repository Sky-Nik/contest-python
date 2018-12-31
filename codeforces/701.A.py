n, a = int(input()), list(map(int, input().split()))

x = (2 * sum(a)) // n

for i in range(n // 2):
	while not a[-1]:
		a.pop()
	al = a[-1]
	p2 = a.index(x - al)
	print(len(a), p2 + 1)
	a.pop()
	a[p2] = 0
