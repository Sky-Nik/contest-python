from collections import deque

n, p1, p2, p3, t1, t2 = map(int, input().split())

d = {1: p1, 2: p2, 3: p3}

LR = [tuple(map(int, input().split())) for _ in range(n)]

q = deque(sorted(
	[(LR[_][0], 'left') for _ in range(n)] + [(LR[_][1], 'right') for _ in range(n)]
))

p, m, t, T = 0, 1, LR[0][0], LR[-1][1]

while q:
	tau, tp = q.popleft()

	if tau > T:
		break

	p += (tau - t) * d[m]

	# print(f'time = {tau}, type = {tp}, mode = {m}, power used = {p}')

	t = tau

	if tp == 'left':
		m = 1
		q = deque(list(filter(lambda _: _[1] in {'left', 'right'}, q)))

	if tp == 'right':
		q.append((tau + t1, 'mode2'))
		q.append((tau + t1 + t2, 'mode3'))
		q = deque(sorted(list(q)))

	if tp == 'mode2':
		m = 2

	if tp == 'mode3':
		m = 3

print(p)
