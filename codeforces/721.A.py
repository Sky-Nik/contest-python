n, s = int(input()), input()

s = 'W' + s + 'W'

k, a = 0, []

for c in s:
	if c == 'B':
		k += 1
	if c == 'W' and k > 0:
		a.append(str(k))
		k = 0

print(len(a))

print(' '.join(a))
