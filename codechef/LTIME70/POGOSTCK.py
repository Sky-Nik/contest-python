t = int(input())

for ti in range(t):
	n, k = map(int, input().split())

	a = list(map(int, input().split()))

	s = [0 for _ in range(n)]

	for i in range(n - 1, -1, -1):
		if i + k < n:
			s[i] = s[i + k] + a[i]
		else:
			s[i] = a[i]

	print(max(s))
