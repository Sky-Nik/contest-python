for _ in range(int(input())):
	a, b, k = map(int, input().split())
	print((a - b) * (k // 2) + (a if k % 2 else 0))
