def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


if __name__ == '__main__':
	a, b, c = map(int, input().split())
	g, x, y = xgcd(a, b)
	if c % g == 0:
		q = -c // g
		print(x * q, y * q)
	else:
		print(-1)
