def h(f, s):
	lf, ls = len(f), len(s) 
	
	if ls < lf:
		return False, ''

	for i in range(ls - lf + 1):
		if s[i:i+lf] == f:
			return True, s[i+lf:]
	
	return False, ''


s, s1, s2 = input(), input(), input()

f, b = h(s2, h(s1, s)[1])[0], h(s2, h(s1, s[::-1])[1])[0]

if f:
	if b:
		print('both')
	else:
		print('forward')
else:
	if b:
		print('backward')
	else:
		print('fantasy')
