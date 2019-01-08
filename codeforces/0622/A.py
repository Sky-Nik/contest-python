from math import sqrt, ceil

n = int(input())

k = ceil((sqrt(1 + 8 * n) - 3) / 2)

print(n - ((k + 1) * k) // 2)
