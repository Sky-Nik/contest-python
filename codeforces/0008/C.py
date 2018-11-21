def dist(p1, p2):
	return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


xys = tuple(map(int, input().split()))

n = int(input())

xyi = [tuple(map(int, input().split())) for i in range(n)]

dp = [(10**9, None) for i in range(2**n)]

dp[0] = (0, None)

for i in range(2**n - 1):
	s = bin(i)[2:]
	s = '0' * (n - len(s)) + s
	s = s[::-1]
	j = s.index('0')
	dsj = dist(xyi[j], xys)
	if dp[i][0] + 2 * dsj < dp[i + 2**j][0]:
		dp[i + 2**j] = (dp[i][0] + 2 * dsj, j)
	for k in range(j + 1, n):
		if s[k] == '0':
			djk = dist(xyi[j], xyi[k])
			dks = dist(xyi[k], xys)
			d = dsj + djk + dks
			if dp[i][0] + d < dp[i + 2**j + 2**k][0]:
				dp[i + 2**j + 2**k] = (dp[i][0] + d, (j, k))

idx = 2**n - 1

print(dp[idx][0])

print('0', end = ' ')
while idx:
	if type(dp[idx][1]) == type(1):
		j = dp[idx][1]
		print(j + 1, '0', end=' ')
		idx -= 2 ** j
	else:
		j, k = dp[idx][1]
		print(j + 1, k + 1, '0', end=' ')
		idx -= 2 ** j + 2 ** k
