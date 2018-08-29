n, k = map(int, input().split())
t = input()

pos = min(filter(lambda x: t[x:] == t[:-x] or x == n, range(n + 1)))

print(t + t[n - pos:] * (k - 1))
