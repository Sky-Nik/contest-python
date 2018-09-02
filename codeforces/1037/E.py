n, m, k = map(int, input().split())

G = [set() for _ in range(n)]

K = set()
len_K = 0

deg_to_v = [set(range(n))] + [set() for _ in range(1, n)]
v_to_deg = [0 for _ in range(n)]


for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].add(v)
    G[v].add(u)

    if u in K and v in K:
        deg_to_v[v_to_deg[u]].remove(u)
        v_to_deg[u] += 1
        deg_to_v[v_to_deg[u]].add(u)

        deg_to_v[v_to_deg[v]].remove(v)
        v_to_deg[v] += 1
        deg_to_v[v_to_deg[v]].add(v)
        print(len_K)
    elif u in K:
        deg_to_v[v_to_deg[v]].remove(v)
        v_to_deg[v] += 1
        deg_to_v[v_to_deg[v]].add(v)

        pass
    elif v in K:
        pass
    else:
        pass


