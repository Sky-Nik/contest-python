# a - white cost, b - black cost
n, a, b = map(int, input().split())

# 0 - white, 1 - black, 2 - none
c = list(map(int, input().split()))

d = c[::-1]

cost = 0

for i in range(n):
    if c[i] == 0:
        if d[i] == 1:
            cost = -2
            break
        else:
            cost += 2 * a
    if c[i] == 1:
        if d[i] == 0:
            cost = -2
            break
        else:
            cost += 2 * b
    if c[i] == 2:
        if d[i] == 0:
            cost += 2 * a
        if d[i] == 1:
            cost += 2 * b
        if d[i] == 2:
            cost += 2 * min(a, b)

print(cost // 2)
