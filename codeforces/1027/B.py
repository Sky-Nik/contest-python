from sys import stdin

n, q = map(int, input().split())
n2 = (n**2 + 1) // 2

l = stdin.read().splitlines()

for i, s in enumerate(l):
    x, y = map(int, s.split())
    if (x ^ y) & 1:
        l[i] = (n2 + (n * (x - 1) + y + 1) // 2)
    else:
        l[i] = (n * (x - 1) + y + 1) // 2

print('\n'.join(map(str, l)))
