def t(n, h):
	if dp[n][h] == -1:
		dp[n][h] = sum(
			t(m - 1, h - 1) * sum(t(n - m, i) for i in range(h)) +
			t(n - m, h - 1) * sum(t(m - 1, i) for i in range(h - 1))
			for m in range(1, n + 1)
		)

	return dp[n][h]


n, h = map(int, input().split())


def fill(i, j):
	if i == 0 and j == 0:
		return 1
	
	if i == 0 or j == 0:
		return 0

	return -1


dp = [[fill(i, j) for j in range(n + 1)] for i in range(n + 1)]

for i in range(n + 1):
	for j in range(n + 1):
		t(i, j)

print(sum(dp[n][i] for i in range(h, n + 1)))
