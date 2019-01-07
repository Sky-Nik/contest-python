n, k = map(int, input().split())
r = list(map(int, input().split()))
xy = [tuple(map(lambda _: int(_) - 1, input().split())) for _ in range(k)]
ir = list(enumerate(r))
ir.sort(key=lambda _: (_[1], _[0]))
a, i, ia = 0, 0, [[ir[0][0], 0]]
for i in range(1, n):
	if ir[i][1] > ir[i - 1][1]:
		a = i
	ia.append([ir[i][0], a])
ia.sort()
for x, y in xy:
	if r[x] > r[y]:
		ia[x][1] -= 1
	if r[x] < r[y]:
		ia[y][1] -= 1
print(*list(map(lambda _: _[1], ia)))
	