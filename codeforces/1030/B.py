n, d = map(int, input().split())

m = int(input())

for _ in range(m):
	xi, yi = map(int, input().split())
	print('YES' if xi + yi >= d and xi + yi <= 2 * n - d and abs(xi - yi) <= d else 'NO')
