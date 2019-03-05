n = int(input())

s = input()

dp = [[(-1 if i != j else 1) for i in range(n)] for j in range(n)]

def f(i, j):
	if i > j:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	
	dp[i][j] = f(i, j - 1) + 1
	for k in range(i, j):
		if s[k] == s[j]:
			dp[i][j] = min(dp[i][j], f(i, k) + f(k + 1, j - 1))

	return dp[i][j]

print(f(0, n - 1))
