n = int(input())
a = list(map(int, input().split()))
dp = dict()
for ai in a:
  if ai not in dp:
    dp[ai] = 0
  if ai - 1 in dp:
    dp[ai] = max(dp[ai], 1 + dp[ai - 1])
k = max(dp.values())
print(k + 1)
l = -1
for ai in a:
  if dp[ai] == k:
    l = ai
idx = []
for i in range(n - 1,-1,-1):
  if a[i] == l:
    idx.append(i + 1)
    l -= 1
print(*idx[::-1])