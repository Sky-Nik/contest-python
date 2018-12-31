n, m = map(int, input().split())

a = 0

for i in range(n):
	f = list(map(int, input().split()))

	for j in range(m):
		if f[2 * j + 1] or f[2 * j]:
			a += 1

print(a)
