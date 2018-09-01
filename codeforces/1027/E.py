mod = 998244353

n, K = map(int, input().split())

dp = [[[0 for k in range(n + 1)] for j in range(n + 1)] for i in range(n + 1)]

dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(n + 1):
            dp[i + 1][j + 1][max(k, j + 1)] += dp[i][j][k]
            dp[i + 1][j + 1][max(k, j + 1)] %= mod
            dp[i + 1][1][max(k, 1)] += dp[i][j][k]
            dp[i + 1][1][max(k, 1)] %= mod

cnt = [sum([dp[n][j][k] for j in range(n + 1)]) % mod for k in range(n + 1)]

pr = [cnt[0]]

for i in range(1, n + 1):
    pr.append(pr[-1] + cnt[i])

ans = sum([cnt[i] * pr[min(n, (K - 1) // i)] for i in range(1, n + 1)]) % mod

ans = ans * ((mod + 1) // 2) % mod

print(ans)
