for _ in range(int(input())):
	s, a, b, c = map(int, input().split())

	k = (s // (a * c))

	o = s - k * a * c

	print(k * (a + b) + o // c)
