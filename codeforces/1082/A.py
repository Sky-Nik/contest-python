from math import ceil


def solve(n, x, y, d):
	if (y - x) % d == 0:
		return abs(y - x) // d
	else:
		l1, l2 = -1, -1
		
		if (y - 1) % d == 0:
			l1 = ceil((x - 1) / d) + (y - 1) // d

		if (n - y) % d == 0:
			l2 = ceil((n - x) / d) + (n - y) // d

		if l1 == -1:
			if l2 == -1:
				return -1
			else:
				return l2
		else:
			if l2 == -1:
				return l1
			else:
				return min(l1, l2)


for _ in range(int(input())):
	n, x, y, d = map(int, input().split())
	print(solve(n, x, y, d))
