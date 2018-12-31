n = int(input())

f = [1, 2]
for _ in range(100):
	f.append(f[-1] + f[-2])

s = ''
for i in range(1, n + 1):
	if i in f:
		s += 'O'
	else:
		s += 'o'

print(s)
