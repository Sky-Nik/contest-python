def valid(a, b, c, d, e):
	s = a + b + c + d + e
	if ((a == 0 and s - a != 1) or 
		(a == 1 and s - a == 1) or
		(b == 0 and s - b != 4) or
		(b == 1 and s - b == 4) or
		(c == 0 and s - c != 3) or
		(c == 1 and s - c == 3) or
		(d == 0 and s - d != 0) or
		(d == 1 and s - d == 0)):
		return False
	return True


for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					if valid(a, b, c, d, e):
						print(f'{a}{b}{c}{d}{e}')