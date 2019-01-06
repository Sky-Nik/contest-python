from math import sqrt, ceil

n = int(input())

a = ceil(sqrt(n))

b = ceil(n / a)

print(a + b)
