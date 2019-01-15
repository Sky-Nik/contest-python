for n in range(10**8):
	if n % 10 == 7:
		s = str(n)
		if 5 * n == int('7' + s[:-1]):
			print(n)
			break
