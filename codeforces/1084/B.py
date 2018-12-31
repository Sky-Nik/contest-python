from math import ceil
import sys

n, s = map(int, input().split())

v = list(map(int, input().split()))

if s > sum(v):
	print(-1)
	sys.exit(0)

m = min(v)

s -= sum(v) - m * n

if s < 0:
	print(m)
	sys.exit(0)

print(m - ceil(s / n))
