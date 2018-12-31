n = int(input())

s = set()

for i in range(n):
	si = input()

	if si in s:
		print('YES')

	else:
		print('NO')

	s.add(si)
