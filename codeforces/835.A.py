s, v1, v2, t1, t2 = map(int, input().split())

T1, T2 = 2 * t1 + s * v1, 2 * t2 + s * v2

if T1 < T2:
	print('First')
elif T1 > T2:
	print('Second')
else:
	print('Friendship')
