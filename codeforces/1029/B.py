n = int(input())

a = list(map(int, input().split()))

ltt2 = [a[i] <= a[i - 1] << 1 for i in range(1, n)]

ans, cur = 0, 0

for i in range(n - 1):
    if ltt2[i] == 1:
        cur += 1
        ans = max(ans, cur)
    else:
        ans = max(ans, cur)
        cur = 0

print(ans + 1)
