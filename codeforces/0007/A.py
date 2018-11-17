c = [input() for _ in range(8)]

h = sum(all(c[_][i] == 'B' for i in range(8)) for _ in range(8))

v = sum(all(c[i][_] == 'B' for i in range(8)) for _ in range(8))

if h == 8 or v == 8:
	print(8)
else:
	print(h + v)
