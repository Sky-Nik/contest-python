n = int(input())

s = [input().split('|') for _ in range(n)]

ok = False

for i in range(n):
	if not ok and s[i][0] == 'OO':
		s[i][0] = '++'
		ok = True
	if not ok and s[i][1] == 'OO':
		s[i][1] = '++'
		ok = True

if not ok:
	print('NO')
else:
	print('YES')
	for i in range(n):
		print('|'.join(s[i]))
