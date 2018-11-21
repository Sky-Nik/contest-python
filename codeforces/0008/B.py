at = (0, 0)

p = [at]

moves = input()

funcs = {
	'L': lambda _: (_[0] - 1, _[1]),
	'R': lambda _: (_[0] + 1, _[1]),
	'D': lambda _: (_[0], _[1] - 1),
	'U': lambda _: (_[0], _[1] + 1),
}

for move in moves:
	at = funcs[move](at)
	p.append(at)

ok = True

for i in range(len(moves) + 1):
	for j in range(len(moves) + 1):
		if abs(i - j) > 1 and abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]) < 2:
			ok = False

print('OK' if ok else 'BUG')
