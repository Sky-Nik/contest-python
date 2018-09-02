n, s = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

m = n // 2

ans = 0

if a[m] > s:
    ans = sum(map(lambda x: max(x - s, 0), a[:m+1]))
if a[m] < s:
    ans = sum(map(lambda x: max(s - x, 0), a[m:]))

print(ans)
