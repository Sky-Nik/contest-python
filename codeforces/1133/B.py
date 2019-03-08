n, k = map(int, input().split())

d = list(map(int, input().split()))

cnt = [0 for _ in range(k)]

for di in d:
	cnt[di % k] += 1

ans = 0
for i in range(1, k):
	ans += min(cnt[i], cnt[k - i])

ans //= 2

ans += cnt[0] // 2

print(2 * ans)