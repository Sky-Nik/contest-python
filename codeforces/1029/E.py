# TLE in codeforces :c


def dfs(v, u, d):
    global p, G
    p[v] = (d, u)
    for w in G[v]:
        if p[w][0] == 0 and w != 1:
            dfs(w, v, d + 1)


n = int(input())

# self, dist, pre
p = {i: (0, None) for i in range(1, n + 1)}

G = {i: set() for i in range(1, n + 1)}

for i in range(n - 1):
    ui, vi = map(int, input().split())
    G[ui].add(vi)
    G[vi].add(ui)

dfs(1, 1, 0)

s = []

for key in p:
    if p[key][0] > 2:
        s.append([key, p[key][0], True])

s.sort(key=lambda x: x[1])

key_to_pos_in_s = {s[i][0]: i for i in range(len(s))}

ans = 0

for j in range(len(s) - 1, -1, -1):
    if s[j][2]:
        ans += 1
        v = s[j][0]
        pv = p[v][1]
        for u in G[pv]:
            if u in key_to_pos_in_s:
                s[key_to_pos_in_s[u]][2] = False
        if pv in key_to_pos_in_s:
            s[key_to_pos_in_s[pv]][2] = False

print(ans)
