n, m = map(int, input().split())

c = list(map(int, input().split()))

a = list(map(int, input().split()))

i, j, k = 0, 0, 0

while i < n and j < m:
	if c[i] <= a[j]:
		j, k = j + 1, k + 1

	i += 1

print(k)
