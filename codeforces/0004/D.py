n, w, h = map(int, input().split())

whi = [list(map(int, input().split())) + [_ + 1, ] for _ in range(n)]

whi.sort(key=lambda _: _[0])

whi = list(filter(lambda _: _[0] > w and _[1] > h, whi))

whi = [(w, h, 0), ] + whi

answer = [(0, 0) for _ in range(n + 1)]

n = len(whi)

for i in range(0, n):
	for j in range(i + 1, n):
		if whi[i][0] < whi[j][0] and whi[i][1] < whi[j][1] and answer[j][0] <= answer[i][0]:
			answer[j] = answer[i][0] + 1, i

if len(whi) > 1:
	pos = list(map(lambda _: _[0], answer)).index(max(map(lambda _: _[0], answer)))

	depth = answer[pos][0]

	path = str(whi[pos][2])
	while answer[pos][1] != 0:
		path = str(whi[answer[pos][1]][2]) + ' ' + path
		pos = answer[pos][1]

	print(depth)
	print(path)
else:
	print(0)
