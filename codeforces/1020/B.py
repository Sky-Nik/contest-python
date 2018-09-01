n = int(input())

p = list(map(lambda x: int(x) - 1, input().split()))

a = [0 for _ in range(n)]

for i in range(n):
    c = [0 for _ in range(n)]
    s = i
    while c[s] == 0:
        c[s] = 1
        s = p[s]
    a[i] = s

print(*list(map(lambda x: x + 1, a)))
