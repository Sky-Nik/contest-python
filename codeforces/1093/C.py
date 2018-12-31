n, b = int(input()), list(map(int, input().split()))

a = [0 for _ in range(n)] 

a[n - 1], a[0] = b[0], 0

for i in range(1, n // 2):
	if a[n - i] < b[i] and b[i] - a[n - i] >= a[i - 1]:
		a[n - 1 - i], a[i] = a[n - i], b[i] - a[n - i]
	else:
		a[n - 1 - i], a[i] = b[i] - a[i - 1], a[i - 1]

print(*a)
