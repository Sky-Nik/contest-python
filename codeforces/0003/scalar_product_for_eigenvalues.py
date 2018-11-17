def A(y):
	return \
		1 * y[0] + 0 * y[1] + 7 * y[2], \
		0 * y[0] + 4 * y[1] + 0 * y[2], \
		5 * y[0] + 0 * y[1] + 1 * y[2]


def scalar(x, y):
	return sum(x[_] * y[_] for _ in range(len(x)))


y = [(1, 0, 0)]
for _ in range(20):
	y.append(A(y[-1]))
	print(f'y_{_} = {y[-1]}')
	print(f'lambda_{_} = {scalar(y[-1], y[-2]) / scalar(y[-2], y[-2])}')
