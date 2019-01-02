def solve(a, b):
	i, j, la, lb = 0, 0, len(a), len(b)
	
	while i < la and a[i] == '0':
		i += 1

	while j < lb and b[j] == '0':
		j += 1

	if la - i > lb - j:
		print('>')
		return
	
	if la - i < lb - j:
		print('<')
		return

	for k in range(la - i):
		if a[i + k] < b[j + k]:
			print('<')
			return
		
		if a[i + k] > b[j + k]:
			print('>')
			return

	print('=')


if __name__ == '__main__':
	a, b = input(), input()

	solve(a, b);
