a = list(map(int, input().split()))

n = len(a)

a.sort()

if all(a[_] + a[_ + 1] < a[_ + 2] for _ in range(n - 2)):
	print('IMPOSSIBLE')
elif all(a[_] + a[_ + 1] <= a[_ + 2] for _ in range(n - 2)):
	print('SEGMENT')
else:
	print('TRIANGLE')
