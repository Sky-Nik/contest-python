n = int(input())

a = list(map(int, input().split()))

d = dict()
for ai in a:
    if ai not in d:
        d[ai] = 0
    d[ai] += 1

l = len(d)

s = set()

ans = 0

for i in range(n):
    ai = a[i]
    if ai not in s:
        s.add(ai)
        d[ai] -= 1
        if d[ai] == 0:
            l -= 1
        ans += l
    else:
        d[ai] -= 1
        if d[ai] == 0:
            l -= 1

print(ans)
