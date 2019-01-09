from math import ceil

n, x, y = map(int, input().split())

a = list(map(int, input().split()))

if x > y:
	print(n)

if x <= y:
	print(ceil(len(list(filter(lambda _: _ <= x, a))) / 2))
