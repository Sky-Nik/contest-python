n = int(input())
p = 0
while (1 << p) <= n:
    p += 1
p -= 1

mod = 10**9 + 7


def f(x, y):
    return n // ((1 << x) * 3**y)


dp = [[[0 for y in range(2)] for x in range(p + 1)] for i in range(n + 1)]
dp[1][p][0] = 1
if (1 << (p - 1)) * 3 <= n:
    dp[1][p - 1][1] = 1

for i in range(1, n):
    for x in range(p + 1):
        for y in range(2):
            dp[i + 1][x][y] += dp[i][x][y] * (f(x, y) - i) 
            dp[i + 1][x][y] %= mod
            if x:
                dp[i + 1][x - 1][y] += dp[i][x][y] * (f(x - 1, y) - f(x, y))
                dp[i + 1][x - 1][y] %= mod
            if y:
                dp[i + 1][x][y - 1] += dp[i][x][y] * (f(x, y - 1) - f(x, y))
                dp[i + 1][x][y - 1] %= mod

print(dp[n][0][0])
