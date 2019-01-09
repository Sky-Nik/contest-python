import sys

inf = 1e10

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
	ans = 1e10

	for l in range(m - 1):
		ans = min(ans, abs(a[0][l] - a[0][l + 1]))

	print(ans)

	sys.exit(0)


diff = {}

for i in range(n):
	for j in range(n):
		if i == j:
			continue

		diff[(i, j)] = inf

		for l in range(m):
			diff[(i, j)] = min(diff[(i, j)], abs(a[i][l] - a[j][l]))

diff2 = {}

for i in range(n):
	for j in range(n):
		if i == j:
			continue

		diff2[(i, j)] = inf

		for l in range(m - 1):
			diff2[(i, j)] = min(diff2[(i, j)], abs(a[i][l] - a[j][l + 1]))

dp = [[[-1 for first in range(n)] for j in range(n)] for i in range(2**n)]

for i in range(n):
	dp[2**i][i][i] = 1e10


def get_dp(i, j, first):
	if dp[i][j][first] != -1:
		return dp[i][j][first]

	bin_i = bin(i)[2:]

	bin_i = bin_i[::-1] + (n - len(bin_i)) * '0'

	prev_i = i - 2**j

	for k in range(n):
		if bin_i[k] == '1' and k != j and (k != first or prev_i == 2**k):
			cur = min(get_dp(prev_i, k, first), diff[(k, j)])

			dp[i][j][first] = max(dp[i][j][first], cur)

	return dp[i][j][first]

ans = 0

for first in range(n):
	for last in range(n):
		if first != last:
			dp_first_last = get_dp(2**n - 1, last, first)
			diff_2_last_first = diff2[(last, first)]
			cur = min(dp_first_last, diff_2_last_first)

			ans = max(ans, cur)

print(ans)
