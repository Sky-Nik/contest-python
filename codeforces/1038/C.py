n = int(input())
a = list(map(lambda x: (int(x), 'A'), input().split()))
b = list(map(lambda x: (int(x), 'B'), input().split()))

c = a + b
c.sort()
c.reverse()

ans = 0

for i in range(2 * n):
    if i % 2 == 0 and c[i][1] == 'A':
        ans += c[i][0]
    if i % 2 == 1 and c[i][1] == 'B':
        ans -= c[i][0]

print(ans)
