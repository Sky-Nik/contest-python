from collections import Counter

n, m = map(int, input().split())

p = sorted(list(map(int, input().split())))

f = [input() for _ in range(m)]

c = sorted(list(Counter(f).values()))

lc, lp = len(c) - 1, len(p) - 1

a = sum(c[lc - _] * p[_] for _ in range(len(c)))

b = sum(c[lc - _] * p[lp - _] for _ in range(len(c)))

print(a, b)
