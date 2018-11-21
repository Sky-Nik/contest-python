def sa(l, r):
	""" sum([l, r)) """
	if r < 0:
		return sa(1 - r, 1 - l)
	elif l < 0:
		return sa(0, 1 - l) + sa(0, r)
	else:
		return (l + r - 1) * (r - l) // 2


n, k = map(int, input().split())

m = list(map(int, input().split()))

used = [[False for _ in range(k)] for _ in range(k)]

xc = yc = k // 2

for mi in m:
	x_o, y_o, d_o = -1, -1, 10**9

	for x in range(k):
		for y in range(k - mi + 1):
			if not any(used[x][y:y+mi]):
				d = mi * abs(x - xc) + sa(y - yc, y + mi - yc)
				if d < d_o:
					x_o, y_o, d_o = x, y, d

	if x_o == -1:
		print(-1)
	else:
		for y in range(y_o, y_o + mi):
			used[x_o][y] = True
		print(x_o + 1, y_o + 1, y_o + mi)
