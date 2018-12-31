n = int(input())

f = list(map(lambda _: int(_) - 1, input().split()))

print('YES' if any(f[f[f[i]]] == i for i in range(n)) else 'NO')
