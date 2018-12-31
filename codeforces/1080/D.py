from math import ceil


def solve(n, k):
	if k == 1:
		return n - 1
	if k == 2:
		if n > 1:
			return n - 1
		else:
			return -1
	if k == 3:
		if n > 2:
			return n - 1
		else:
			return -1
	if k in {4, 5}:
		if n > 1:
			return n - 2
		else:
			return -1

	if 2 * n + 1 <= len(bin(3 * k)[2:]):
		return -1
	else:
		return n - ceil((len(bin(3 * k)[2:]) - 1) / 2)


for i in range(int(input())):
	n, k = map(int, input().split())
	a = solve(n, k)
	if a == -1:
		print('NO')
	else:
		print('YES', a)
