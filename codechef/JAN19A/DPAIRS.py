n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))


a = sorted([(a[_], _) for _ in range(n)])

b = sorted([(b[_], _) for _ in range(m)])


for _ in range(n):
	print(a[_][1], b[0][1])

for _ in range(1, m):
	print(a[-1][1], b[_][1])
