n = int(input())

a, b = 0, 0

for _ in range(n):
	t, x, y = map(int, input().split())

	if t == 1:
		a += x - y
	if t == 2:
		b += x - y

print('LIVE' if a >= 0 else 'DEAD')

print('LIVE' if b >= 0 else 'DEAD')
