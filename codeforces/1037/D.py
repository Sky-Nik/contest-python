from collections import deque

n = int(input())

G = {v: set() for v in range(1, n + 1)}

for i in range(1, n):
    u, v = map(int, input().split())
    G[u].add(v)
    G[v].add(u)

q = list(map(int, input().split()))

current = q[0]

qq = deque()
qq.append(current)

OK = True

for v in q[1:]:
    if v in G[current]:
        qq.append(v)
    else:
        while v not in G[current] and qq:
            current = qq.popleft()
        if v not in G[current]:
            OK = False
        if v in G[current]:
            qq.append(v)

print('Yes' if OK else 'No')
