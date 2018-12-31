for _ in range(int(input())):
	s = input()
	f = sorted(s)
	if f == f[::-1]:
		print(-1)
	else:
		print(''.join(f))
